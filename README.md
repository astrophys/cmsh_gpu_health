# cmsh_gpu_health
This code is used to trawl through historic GPU temperature data from cmsh
to find GPUs that have exceeded 80C in the past week.


## Usage :
    ```
    # Collect data
    mkdir -p data/YYYYMMDD
    cd data/YYYYMMDD
    
    # Set node name prefix, e.g. if nodes are named node[01-31]
    export HOSTSTEM=node
    
    bash ../../src/collect_data.sh
    cd -
    
    # Run code
    ml load python/3.13
    python src/cmsh_gpu_health.py --path data/YYYYMMDD
    ```
