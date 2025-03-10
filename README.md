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
Nextflow 24.10.5 is available - Please consider updating your version to it
N E X T F L O W  ~  version 23.10.0
Launching `https://github.com/maxibor/nf-admix` [amazing_liskov] DSL2 - revision: 1ca446bdd8 [master]
Downloading plugin nf-schema@2.2.0
--help         [boolean, string] Show the help message for all top level parameters. When a parameter is given to `--help`, the full help message of that parameter
will be printed.
--helpFull     [boolean]         Show the help message for all non-hidden parameters.
--showHidden   [boolean]         Show all hidden parameters in the help message. This needs to be used in combination with `--help` or `--helpFull`.

Input/output options
  --vcf        [string]  Path to VCF file
  --k_min      [integer] Minimum number of clusters [default: 3]
  --k_max      [integer] Maximum number of clusters [default: 5]
  --outdir     [string]  The output directory where the results will be saved. You have to use absolute paths to storage on Cloud infrastructure.
[default: results]

 !! Hiding 3 param(s), use the `--showHidden` parameter to show them !!
------------------------------------------------------
```

### Input/output options

Define where the pipeline should find input data and save output data.

| Parameter | Description | Type | Default | Required | Hidden |
|-----------|-----------|-----------|-----------|-----------|-----------|
| `vcf` | Path to VCF file | `string` |  |  |  |
| `k_min` | Minimum number of clusters | `integer` | 3 |  |  |
| `k_max` | Maximum number of clusters | `integer` | 5 |  |  |
| `outdir` | The output directory where the results will be saved. You have to use absolute paths to storage on Cloud infrastructure. | `string` | results | True |  |

### Other parameters

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
