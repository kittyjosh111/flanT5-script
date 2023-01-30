Some scripts to do text generation using FlanT5 and Hugging Face Transformers. Ensure you have a lot of RAM to run these. Also, the scripts only use CPU as they were originally run on Oracle Cloud's Free Tier, which does not have GPU support.

First use pip to install the ```requirements.txt```, then you can select which script to run. It will ask you for your prompt. Small, middle, and large indicate larger lengths and temperature values in their respective orders.

An example is as follows: Note I am using venv on ubuntu.

```
(venv) ubuntu@oracle:~/dev/flanT5-script$ python3 flanT5_fast.py 
Put in your prompt: How was your day today?
It was a good day for me because I didn't have to go to work today.
```