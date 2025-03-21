process PLOT_ADMIXTURE {
    tag "$meta.id"
    label 'process_low'

    conda "${moduleDir}/environment.yml"
    container "${ workflow.containerEngine == 'singularity' && !task.ext.singularity_pull_docker_container ?
        'oras://community.wave.seqera.io/library/pip_pandas_plotnine:ae33577ad40c29b5' :
        'biocontainers/pydamage:0.70--pyhdfd78af_0' }"

    input:
    tuple val(meta), path(q), path(log)

    output:
    tuple val(meta), path("*.png"), emit: png
    tuple val(meta), path("*.svg"), emit: svg

    when:
    task.ext.when == null || task.ext.when

    script:
    def args = task.ext.args ?: ''
    def prefix = task.ext.prefix ?: "${meta.id}"
    """
    plot_admix.py \\
        $args \\
        ${prefix}
    """
}
