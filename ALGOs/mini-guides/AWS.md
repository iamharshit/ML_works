## AWS or Amazon Web Service

Cloud platform provided by amazon.

AWS ec2 version is used for training our NNet on cloud.

## Why we need GPUs?

Training could take anywhere from 15 minutes to several hours, depending on the number of epochs, the size of the neural networks and other factors.

A faster alternative is to train on a GPU (Graphics Processing Unit). While a CPU can calculate more complex operations than a GPU, it has a small throughput. This is why GPU's are so much faster when training neural networks than CPUs. They do more calculations at the same time, which is important when working with big data.

## AWS Usage

* Create an AWS account from [here](https://aws.amazon.com/) and go for free basic plan.We need to provide Credit or Debit info for verification purpose only.They also use this card as the payment method for any services not covered by the credits/free-tier. 
* Set the GPU you need.
* Start JUpyter notebook on AWS and start to code.Whenever you run any cell it would automatically be computeed on GPU.

## What is EC2 ?

EC2 or Elastic Compute Cloud is one of the many services provided by Amazon.This lets us to create virtual servers technically called as instances.We can use these virtual servers to run our code on GPU.

There are many virtual servers varying from small to large GPU available on EC2, we generally go for "g2.2xlarge".

By default the GPU limit is set to 0 for each instance or virtual server, we can increase it to the desired value by submitting a request.Then we need to wait until AWS approves your Limit Increase Request. AWS typically approves these requests within 48 hours.After request approval 'Launch an Instance' from [here](https://console.aws.amazon.com/ec2/v2/home).

## Launching an Instance

After Launching instance we need to select the enviornment files for running our GPU technically called as [Amazon Web Images](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html).Go for AWI containing cuDNN, Tensorflow, python 2.7 and desired packages.

Select the storage size(generally 32GB choosen).After all these changes click on the 'Launch' button and go on the 'view instance' button to view your instance running.Most importantly, remember to “stop” (i.e. shutdown) your instances when you are not using them. Otherwise, your instances might run for a day, week, month, or longer without you remembering, and you’ll wind up with a large bill!

## Logging in

After Launching an instance we need to log in into amazon by ssh-ing to IP address provided.Then we need to do `source activate dl` to activate new enviornment.Now we can run any code from terminal and it would be executed on AWS.

## AWS Educate

For GPU usage activate your AWS Educate account to make it free.

## Alternative to AWS

We can buy our own NVIDIA GPU.But there's more to it than just plugging the GPU into the machine. Even if you have the knowledge to install a GPU, there's hurdles to getting CUDNN installed properly. This is why it isn't recommend to use your own GPU.Instead go for Amazon EC2 instance.


