## 
This is an implementation of the papers:
[Hiding speaker's sex in speech using zero-evidence speaker representation in an analysis/synthesis pipeline](https://arxiv.org/abs/2211.16065)


The authors are Paul-Gauthier Noé, Xiaoxiao Miao, Xin Wang, Junichi Yamagishi, Jean-François Bonastre, Driss Matrouf

Please cite these papers if you use this code.

This code is adapted from [SSL-SAS](https://github.com/nii-yamagishilab/SSL-SAS/)


- Generate protected speech
  1. Download English development and evaluation data provided by the [VoicePrivacy2020 Challenge](https://github.com/Voice-Privacy-Challenge/Voice-Privacy-Challenge-2020): [LibriSpeech](http://www.openslr.org/12/)-subsets (libri_dev and libri_test). Just run `bash adapted_from_vpc/00_download_testdata.sh`. The user will be requested the password, please contact [VoicePrivacy2020 Challenge organizers](https://github.com/Voice-Privacy-Challenge/Voice-Privacy-Challenge-2020).
  2. Generate anonymized speech: `bash scripts/scripts/demo_synth_protect.sh`.

- Train a HiFi-GAN using [LibriTTS-100h](https://www.openslr.org/60/) on your own: `bash scripts/scripts/train_hifigan.sh`

Pretrained models can be found here: https://zenodo.org/record/7347685#.Y4cS0i8Rp0t


## Dependencies
`git clone https://github.com/nii-yamagishilab/speaker_sex_attribute_privacy.git`

`cd speaker_sex_attribute_privacy`

`bash scripts/install.sh`

Make sure sox and parallel are installed. 
## 



## Audio examples
original | proposed | global | TDPSOLA | synthesised but non protected*
--- | --- | --- | --- | ---
 [ex1](https://user-images.githubusercontent.com/18285855/203569403-3f38c56f-8d26-4f82-9e9b-3a220a1126b4.mp4) | [ex1](https://user-images.githubusercontent.com/18285855/203569752-de9ec3a8-ed03-40ab-b90d-d1c8f0ff042e.mp4) | [ex1](https://user-images.githubusercontent.com/18285855/203570240-8e8fc966-9dba-4888-8339-f1890f20a003.mp4) | [ex1](https://user-images.githubusercontent.com/18285855/203570564-84e1047b-290a-45f6-8824-ef868d1fac2b.mp4) | [ex1](https://user-images.githubusercontent.com/18285855/203570796-abb2b989-a30c-463d-a91d-877ac13ba549.mp4)
 [ex2](https://user-images.githubusercontent.com/18285855/203569539-447f1820-0020-41a4-b5c9-362bb7fe45a0.mp4) | [ex2](https://user-images.githubusercontent.com/18285855/203569772-30804af4-fb19-42bb-95d6-8c8509ace46c.mp4) | [ex2](https://user-images.githubusercontent.com/18285855/203570260-32474cba-c178-4d26-91ac-cef291e8dab8.mp4) | [ex2](https://user-images.githubusercontent.com/18285855/203570581-0a5d87a4-effb-449c-93a3-f91e78f02dde.mp4) | [ex2](https://user-images.githubusercontent.com/18285855/203570810-e6b85343-6f9f-491b-9362-26503148a627.mp4)
 [ex3](https://user-images.githubusercontent.com/18285855/203569593-d8d67f28-460a-42a0-8dd9-039867915082.mp4) | [ex3](https://user-images.githubusercontent.com/18285855/203569793-22f9cca5-308a-40bb-953c-81b644c78c55.mp4) | [ex3](https://user-images.githubusercontent.com/18285855/203570272-5434e8ad-1640-45a2-a690-8028afe7999a.mp4) | [ex3](https://user-images.githubusercontent.com/18285855/203570592-72628802-d061-4409-90aa-f28a1eeef25e.mp4) | [ex3](https://user-images.githubusercontent.com/18285855/203570825-abd69fb1-7018-4bf8-9486-849010e0ee8e.mp4)
 [ex4](https://user-images.githubusercontent.com/18285855/203569648-7be3d50e-b793-49a7-819f-12de6b6e9a59.mp4) | [ex4](https://user-images.githubusercontent.com/18285855/203569808-5d15970a-6ecf-4ea3-934f-e7a780f71b17.mp4) | [ex4](https://user-images.githubusercontent.com/18285855/203570288-d1909e45-ea46-4696-bda1-7a204f75fc6d.mp4) | [ex4](https://user-images.githubusercontent.com/18285855/203570605-084cf740-4bac-4d68-aaac-e5812b9f9ea1.mp4) | [ex4](https://user-images.githubusercontent.com/18285855/203570837-b8d14511-e96e-4d0c-8a72-dd86de8c328b.mp4)

*The speech has been fed into the proposed system but without applying the protectection (i.e. without xvector and pitch transformation)

The original audio samples are from [LibriSpeech](https://www.openslr.org/12) under Attribution 4.0 International (CC BY 4.0) license.
##

## License

The `adapted_from_facebookreaserch` subfolder has [Attribution-NonCommercial 4.0 International License](https://github.com/nii-yamagishilab/SSL-SAS/blob/main/adapted_from_facebookresearch/LICENSE). The `adapted_from_speechbrain` subfolder has [Apache License](https://github.com/nii-yamagishilab/SSL-SAS/blob/main/adapted_from_speechbrain/LICENSE). They were created by the [facebookreasearch](https://github.com/facebookresearch/speech-resynthesis/blob/main) and [speechbrain](https://github.com/speechbrain/speechbrain) orgnization, respectively. The `scripts` subfolder has the [MIT license](https://github.com/nii-yamagishilab/SSL-SAS/blob/main/scripts/LICENSE).

Because this source code was adapted from the facebookresearch and speechbrain, the whole project follows  
the [Attribution-NonCommercial 4.0 International License](https://github.com/nii-yamagishilab/SSL-SAS/blob/main/adapted_from_facebookresearch/LICENSE).

Copyright (c) 2022, Yamagishi Laboratory, National Institute of Informatics.
All rights reserved.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
