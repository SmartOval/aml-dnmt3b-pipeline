nextflow.enable.dsl=2

include { PREPROCESS_AML; SUMMARIZE_AML } from './modules/aml_pipeline.nf'

workflow {
    input_ch = Channel.fromPath("data/test/*.csv")
                      .map { file -> file }

    cleaned_ch = PREPROCESS_AML(input_ch)
    SUMMARIZE_AML(cleaned_ch)
}
