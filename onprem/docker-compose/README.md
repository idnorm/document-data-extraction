# Docker compose

This folder holds the simplest version of deploying our solution using docker compose.

> ⚠️ We **DO NOT** recommend using this in highly concurrent, high load production environments.
For such purpases we recommend using our helm chart and scaling it using kubernetes.

> Docker images expect x86 CPU architecture, or in docker terms `linux/amd64` platform, currently we do not support ARM or Apple silicon platforms.

It starts `3` services

 - `model-dl` - which downloads the model to the machine
 - `serving` - which runs AI models inference
 - `extraction` - the main entrypoint, this is what your code with communicate with

The docker compose file is configurable by env vars. You can set them either in your command line or using `.env` file. 

We set the default values in the `.env` file that work out of the box.

The only value that you **MUST** specify is `IDEX_LICENSE_KEY`, this must be set to the license key you acquired for our service. 

Depending on your CPU architecture you might need to specify a different vale for `SERVING_TAG`. By default, we specify `-skylake`, but if you are running on an older CPU you might need to specify `-haswell` or `-broadwell`.

To start simply position yourself in this directory and run the 

``` bash 
docker compose up -d
```

Once started, the solution endpoint will be available for your application integration at localhost on port `8005` (or whicherver port you specified in `.env` file). 
You can inspect the logs using 

```bash
docker compose logs extraction -f
```

Once you see 
```text
some example text
```

the service is ready to accept and process requests.