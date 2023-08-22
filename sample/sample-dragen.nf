nextflow.enable.dsl = 2

params.ref_tar = "NO_TAR"
params.read1 = "NO_READ1"
params.read2 = "NO_READ2"
params.sample_id = "dragen"

process DRAGEN {

    container '102576526753.dkr.ecr.us-east-1.amazonaws.com/dragen/dragen:3.9.5-159'
    pod annotation: 'scheduler.illumina.com/presetSize', value: 'fpga-medium'

    publishDir "out", mode: "copy"

    input:
        tuple path(read1),path(read2)
        val sample_id
        path ref_tar

    output:
        stdout emit: result
        path '*', emit: output

    script:
        """
        set -ex
        mkdir -p /scratch/reference
        tar -C /scratch/reference -xf ${ref_tar}
        
        /opt/edico/bin/dragen --partial-reconfig HMM --ignore-version-check true
        /opt/edico/bin/dragen --lic-instance-id-location /opt/instance-identity \\
            --output-directory ./ \\
            -1 ${read1} \\
            -2 ${read2} \\
            --intermediate-results-dir /scratch \\
            --output-file-prefix ${sample_id} \\
            --RGID ${sample_id} \\
            --RGSM ${sample_id} \\
            --ref-dir /scratch/reference \\
            --enable-variant-caller true
        """
}

workflow {
    DRAGEN(
        Channel.of([file(params.read1), file(params.read2)]),
        Channel.of(params.sample_id),
        Channel.fromPath(params.ref_tar)
    )
}