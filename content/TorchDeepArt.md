Title: Adventures in Torch	and Deep Art
Date: 2018-11-11 00:26
Category: Deep Learning
Tags: GPU, Torch, Photography, Deep Learning
Slug: TorchDeepArt
Authors: Vincent Croft
Summary: I setup torch with OpenCL to use the GPU on my laptop to make pretty pictures. Then I scaled the problem up on Google Cloed Conmpute Engine.

# Adventures in Torch	and Deep Art
Recently I made a hanging canvas made for my Mother in law based on the idea of deep style transfer.

After several attempts with various implemetations of the code I settled on torch implementation of the paper [A Neural Algorithm of Artistic Style](http://arxiv.org/abs/1508.06576) by Leon A. Gatys, Alexander S. Ecker, and Matthias Bethge as implemented by [Justin Johnson](https://github.com/jcjohnson). 

For the last 2 years I've been lugging around my 15inch macbook pro - 4 times the weight and twice the price of a mac that would accomodate most of my needs... but this one has a dedicated GPU! ...but... that GPU is an intel Radeon Pro 450 and therefore not CUDA compatible and therefore not useful for machine learning.

Torch is a lua front end to the TH tensor processing library and a predecessor to pytorch. Unlike pytorch however, Torch supports OpenCL execution and thereby makes my computer useful again! This allowed me to directly observe what all this fuss about GPU programming is about... about a 50 times speed upgrade! 

But even this new found magical power had its limitations. The image being manipulatied cannot be larger than 1024x1024 or else the GPU runs out of memory.

Enter the power of the cloud. Setting up torch on GCP was not as straight forward as id like but given that I did it 16 times in an afternoon I think it cant have been that bad.

<img src="https://raw.githubusercontent.com/vincecr0ft/vincecr0ft.github.io/source/content/images/montbug.png" height="400px">

Want to give it a try?
## Torch + CUDA on Google Cloud Platform


I launched the session As I was taught during my tesor flow certification. I navigatied to [the Google Cloud Console](https://console.cloud.google.com) and started a ubuntu instance. Living in europe I found the only site to reliably provide me with GPU instances was the Belgian host at `europe-west1-b` first I ran out of swap space when trying to install [`cudnn`](https://developer.nvidia.com/cudnn) and had to boot up a new instance. I had numerous problems when trying to use a dedicated deeplearning image (pytorch or tensorflow) so I stuck to plain ubuntu 16.04 with a couple of CPUs and at least 4 GPUs (I also tried with just one but ran into the same memory issues as when running locally):

```
$ gcloud compute --project 'your-project-name' ssh --zone 'your-zone' 'your-instance-name'
```

once in the instance i followed steps to install CUDA:

```
$ curl -O http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
$ sudo dpkg -i cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
$ sudo apt-get update
$ rm cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
$ sudo apt-get install cuda-8-0
```

Then installed torch7 - hopefully picking up the CUDA install:

```
$ git clone https://github.com/torch/distro.git ~/torch --recursive

$ cd ~/torch; bash install-deps;

$ ./install.sh
```

this can take a while - especially if your CUDA istallation succeeded. I did have some minor issues with OpenBlas but nothing a quck google and some Ubuntu-fu can't fix.

Finally (before checking out the main repo) we need loadcaffe to load a pretrained model from the Caffe Model Zoo:

```
$ sudo apt-get install libprotobuf-dev protobuf-compiler
$ sudo ~/torch/install/bin/luarocks install loadcaffe
``` 

Now its time for the actual code!

## Neural Style

the readme for this code is great and the examples folder is great. Just check it out and run it!

```
$ git clone https://github.com/jcjohnson/neural-style.git
$ cd neural_style; sh models/download_models.sh;
$ th neural_style.lua -style_image <image.jpg> -content_image <image.jpg>
```

but wait! that last step needs local images! how do I get them onto the GCP instance? [Cloud SDK](https://cloud.google.com/sdk/). *LOCALLY* download the code for your system and run:

```
$ ./google-cloud-sdk/install.sh
```
Restart your terminal

```
$ gcloud init

```
and log in! Now we can do an scp:

```
$ gcloud compute scp /folder-to-your-file-locally/image.jpg instance-name:/tmp/
```

whist there are lots of fun tutorials out there, and playing around with all the possible inputs and styles is crazy addictive, I found the [starry_stanford.sh](https://github.com/jcjohnson/neural-style/blob/master/examples/multigpu_scripts/starry_stanford.sh) script gave the best results but needs some mighty powerful GPUs or to step down to CPU only mode in the end.

<img src="https://raw.githubusercontent.com/vincecr0ft/vincecr0ft.github.io/source/content/images/montbug.png" height="400px">

Oh and I think Im still on the GCP free/trial tier so it still says that I have 0 estimated costs.