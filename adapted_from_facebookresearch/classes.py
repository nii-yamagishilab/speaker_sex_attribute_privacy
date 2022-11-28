import numpy as np
import torch
import torch.nn as nn    
import torch.nn.functional as F
from torch.utils import data
from torch import distributions as D
from math import log
from torch.nn.parameter import Parameter

class Rescale(nn.Module):
    def __init__(self, dim):
        super(Rescale, self).__init__()
        self.weight = nn.Parameter(torch.zeros(dim))

    def forward(self, x):  
        x = self.weight * x
        return x


class Linear(nn.Module):

    def __init__(self, in_features: int, out_features: int, bias: bool = True,
                 device=None, dtype=None):
        super(Linear, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.weight = Parameter(torch.zeros((out_features, in_features)))
        self.bias = Parameter(torch.zeros(out_features))

    def forward(self, x):
        return F.linear(x, self.weight, self.bias)






class CouplingLayer(nn.Module):
    def __init__(self, input_dim, hidden_dim, mask):
        super(CouplingLayer, self).__init__()
    
        self.input_dim      = input_dim
        self.hidden_dim     = hidden_dim
        self.s              = nn.Sequential(nn.Linear(input_dim, hidden_dim), nn.LeakyReLU(), nn.Linear(hidden_dim, hidden_dim), nn.LeakyReLU(), nn.Linear(hidden_dim, input_dim), nn.Tanh(), Rescale(input_dim))
        self.t              = nn.Sequential(nn.Linear(input_dim, hidden_dim), nn.LeakyReLU(), nn.Linear(hidden_dim, hidden_dim), nn.LeakyReLU(), Linear(hidden_dim, input_dim))
        self.mask           = nn.Parameter(mask, requires_grad=False)



    def f(self, x):             # from x to y
        x1          = x*self.mask
        s1          = self.s(x1)
        t1          = self.t(x1)
        log_detJ    = torch.sum(s1*(1-self.mask),dim=1)
        return x1+(1-self.mask)*(x*torch.exp(s1)+t1), log_detJ

    def g(self, y):              # from y to x
        y1 = y*self.mask
        s1 = self.s(y1)
        t1 = self.t(y1)
        return y1+(1-self.mask)*(y-t1)*torch.exp(-s1)



class RealNVP(nn.Module):

    def __init__(self,input_dim, hidden_dim, masks, muinit):
        super(RealNVP, self).__init__()

        self.input_dim  = input_dim
        self.masks      = masks
        self.cpl        = nn.ModuleList([CouplingLayer(input_dim, hidden_dim, masks[i]) for i in range(len(masks))])
        self.lmu         = nn.Parameter(torch.tensor(log(muinit)))
        print(len(self.masks))

    def log_prior(self, z, l):
        i0  = l==0
        i1  = l==1
        i0  = i0.reshape((len(i0),))
        i1  = i1.reshape((len(i1),))
        m  = torch.zeros(self.input_dim).cuda()
        m[0] = torch.exp(self.lmu)
        C = torch.eye(self.input_dim).cuda()
        C[0,0] = 2*torch.exp(self.lmu)
        prior0  = D.MultivariateNormal(m, C)
        prior1  = D.MultivariateNormal(-m, C)
        lp0 = prior0.log_prob(z[i0])
        lp1 = prior1.log_prob(z[i1])

        return torch.cat((lp0,lp1)), torch.exp(self.lmu)


    def f(self, x):      # from x to z
        log_detJ = 0
        z = x
        for i in (range(len(self.masks))):
            z, log_detJi = self.cpl[i].f(z)
            log_detJ += log_detJi
        return z, log_detJ

    def g(self, z):      # from z to x
        for i in reversed(range(len(self.masks))):
            z = self.cpl[i].g(z)
        x = z
        return x 
