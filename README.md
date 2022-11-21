## 
This is an implementation of the papers:
Hiding speaker's sex in speech using zero-evidence speaker representation in an analysis/synthesis pipeline

The authors are Paul-Gauthier Noé, Xiaoxiao Miao, Xin Wang, Junichi Yamagishi, Jean-François Bonastre, Driss Matrouf

Please cite these papers if you use this code.

This code is adapted from [SSL-SAS](https://github.com/nii-yamagishilab/SSL-SAS/)


- Generate protected speech
  1. Download English development and evaluation data provided by the [VoicePrivacy2020 Challenge](https://github.com/Voice-Privacy-Challenge/Voice-Privacy-Challenge-2020): [LibriSpeech](http://www.openslr.org/12/)-subsets (libri_dev and libri_test). Just run `bash adapted_from_vpc/00_download_testdata.sh`. The user will be requested the password, please contact [VoicePrivacy2020 Challenge organizers](https://github.com/Voice-Privacy-Challenge/Voice-Privacy-Challenge-2020).
  2. Generate anonymized speech: `bash scripts/scripts/demo_synth_protect.sh`.

- Train a HiFi-GAN using [LibriTTS-100h](https://www.openslr.org/60/) on your own: `bash scripts/scripts/train_hifigan.sh`


Audio samples can be found here: Coming soon

Pretrained models can be found here: Coming soon


## Dependencies
`git clone https://github.com/nii-yamagishilab/speaker_sex_attribute_privacy.git`

`cd speaker_sex_attribute_privacy`

`bash scripts/install.sh`

Make sure sox and parallel are installed. 
## 


## License

The `adapted_from_facebookreaserch` subfolder has [Attribution-NonCommercial 4.0 International License](https://github.com/nii-yamagishilab/SSL-SAS/blob/main/adapted_from_facebookresearch/LICENSE). The `adapted_from_speechbrain` subfolder has [Apache License](https://github.com/nii-yamagishilab/SSL-SAS/blob/main/adapted_from_speechbrain/LICENSE). They were created by the [facebookreasearch](https://github.com/facebookresearch/speech-resynthesis/blob/main) and [speechbrain](https://github.com/speechbrain/speechbrain) orgnization, respectively. The `scripts` subfolder has the [MIT license](https://github.com/nii-yamagishilab/SSL-SAS/blob/main/scripts/LICENSE).

Because this source code was adapted from the facebookresearch and speechbrain, the whole project follows  
the [Attribution-NonCommercial 4.0 International License](https://github.com/nii-yamagishilab/SSL-SAS/blob/main/adapted_from_facebookresearch/LICENSE).

Copyright (c) 2022, Yamagishi Laboratory, National Institute of Informatics.
All rights reserved.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
