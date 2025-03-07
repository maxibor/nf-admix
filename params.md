#  pipeline parameters



## Input/output options

Define where the pipeline should find input data and save output data.

| Parameter | Description | Type | Default | Required | Hidden |
|-----------|-----------|-----------|-----------|-----------|-----------|
| `vcf` | Path to VCF file | `string` |  |  |  |
| `k_min` | Minimum number of clusters | `integer` | 3 |  |  |
| `k_max` | Maximum number of clusters | `integer` | 5 |  |  |
| `outdir` | The output directory where the results will be saved. You have to use absolute paths to storage on Cloud infrastructure. | `string` | results | True |  |

## Other parameters

| Parameter | Description | Type | Default | Required | Hidden |
|-----------|-----------|-----------|-----------|-----------|-----------|
| `publish_dir_mode` |  | `string` | copy |  | True |
| `custom_config_version` |  | `string` | master |  | True |
| `custom_config_base` |  | `string` | https://raw.githubusercontent.com/nf-core/configs/master |  | True |
