# nf-admix

Simple nextflow pipeline to run unsupervised [ADMIXTURE](https://dalexander.github.io/admixture) from a VCF file.
It is assumed that the input VCF has already been filtered, and that variants are not under Linkage Desequilibrium.


## Install

```bash
nextflow pull maxibor/nf-admix
```

## Run

```
nextflow run maxibor/nf-admix --vcf /path/to/vcf --k_min 3 --k_max 5
```

## Help

```
$ nextflow run maxibor/nf-admix --help
```

## Input/output options                                                                                                     
                                                                                                                            
Define where the pipeline should find input data and save output data.                                                      
                                                                                                                            
| Parameter | Description | Type | Default | Required | Hidden |                                                            
|-----------|-----------|-----------|-----------|-----------|-----------|                                                   
| `vcf` | Path to VCF file | `string` |  |  |  |                                                                            
| `k_min` | Minimum number of clusters | `integer` | 3 |  |  |                                                              
| `k_max` | Maximum number of clusters | `integer` | 5 |  |  |                                                              
| `outdir` | The output directory where the results will be saved. You have to use absolute paths to storage on Cloud       
infrastructure. | `string` | results | True |  |                                                                            
| `const_fid` | Set a constant plink family ID. | `number` |  |  |  |                                                       
                                                                                                                            
## Other parameters                                                                                                         
                                                                                                                            
| Parameter | Description | Type | Default | Required | Hidden |                                                            
|-----------|-----------|-----------|-----------|-----------|-----------|                                                   
| `publish_dir_mode` |  | `string` | copy |  | True |                                                                       
| `custom_config_version` |  | `string` | master |  | True |                                                                
| `custom_config_base` |  | `string` | https://raw.githubusercontent.com/nf-core/configs/master |  | True |                 
                                                                                                                            


## Test

```
nextflow run maxibor/nf-admix -profile {docker,singularity,conda},test
```


## Acknowledgments
- This pipeline reimplements the example from the speciationgenomics ADMIXTURE tutorial: [speciationgenomics.github.io/ADMIXTURE](https://speciationgenomics.github.io/ADMIXTURE/)
- This pipeline uses [nf-core modules](https://nf-co.re/modules/)