# nf-admix

Simple nextflow pipeline to run unsupervised [ADMIXTURE](https://dalexander.github.io/admixture) from a VCF file.
It is assumed that the input VCF has already been filtered, and that variants are not under Linkage Desequilibrium.


## Install

```bash
nextflow pull maxibor/nf-admix
```

## Run

```
nextflow run maxibor/nf-admix --vcf /path/to/vcf --k_min 3 --k_min 5
```

## Test

```
nextflow run maxibor/nf-admix -profile {docker,singularity,conda},test
```


## Acknowledgments
This pipeline reimplements the example from the speciationgenomics ADMIXTURE tutorial: [speciationgenomics.github.io/ADMIXTURE](https://speciationgenomics.github.io/ADMIXTURE/)
