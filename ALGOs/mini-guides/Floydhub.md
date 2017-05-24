## Floydhub 

It is an high level abstraction of AWS.Other then training a NNet we can even deploy models on floydhub.Unlike AWS where the requirements needs to be installed manually, floydhub automatically sets up requirement in the instance.

## Steps:

1. Do login `floyd login`.Set up the enviornment using Web browser or from CLI by `floyd run --mode jupyter --gpu --env tensorflow-1.0`.
2. Go to the project directory and initialise floyd `floyd init <my_project>`
3. Run the project script ` floyd run "python test.py" --<mode>` or `floyd run --mode jupyter`.Note: the mode can be `cpu` or `gpu`.
4. After the script is completly executed or jupyter notebook's work is done to stop an instance do `floyd stop <run_ID>`.Get the run_ID from `floyd status`.To get more info about an instance do `floyd info <run_ID>`.
5. To view the output on floyd do `floyd output run_ID` 

## Data on floyd:

Most of the popular dataset are available on floyd [here](http://docs.floydhub.com/guides/datasets/), so we neednot put them on floyd instead we can directly reference them during running the script `floyd run "python train.py" --data <dataset_ID>`.The dataset will be available at `/input/<dataset_name>`. So, the CIFAR10 data will be in `/input/CIFAR10`.
