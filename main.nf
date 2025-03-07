include { PLINK_VCF } from './modules/nf-core/plink/vcf/main'
include { ADMIXTURE  } from './modules/nf-core/admixture/main'
include { validateParameters; paramsSummaryLog } from 'plugin/nf-schema'

// Validate input parameters
validateParameters()

// Print summary of supplied parameters
log.info paramsSummaryLog(workflow)

workflow {
    
    ch_components = Channel.of(params.k_min..params.k_max)
    ch_vcf = Channel.fromPath(params.vcf).map{
        return [
            ['id': it.getSimpleName()],
            it
        ]
    }

    PLINK_VCF(ch_vcf)

    ch_admix = PLINK_VCF.out.bed
        .join(PLINK_VCF.out.bim)
        .join(PLINK_VCF.out.fam)
        .combine(ch_components).map {
            meta, bed, bim, fam, k ->
            def new_meta = meta.clone()
            new_meta['k'] = k
            [
                new_meta,
                bed,
                bim,
                fam,
                k
            ]
        }

    ADMIXTURE(ch_admix)

    



}