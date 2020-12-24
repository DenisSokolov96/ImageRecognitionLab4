import ImageComparasion as comparasion
import Metrics as metrics

#сравнение картинок
def funcComparasion():
    orig_file_list = ["AMDTest/SU4.bmp", "Berlin/SU4.bmp", "Gladiolus/SU4.bmp"]
    folders_list = ["\AMDTest", "\Berlin", "\Gladiolus"]
    comparasion.do_comparation(orig_file_list, folders_list)


#признаки
def funcSign():
    metrics.WriteToFile("\Berlin_4", metrics.calcContrast, metrics.calc_RMS_Contrast, metrics.calc_CustomMetric,
                        metrics.calc_CustomMetric_dsp, metrics.calc_CustomMetric_b)
    metrics.WriteToFile("\AmdTest_4", metrics.calcContrast, metrics.calc_RMS_Contrast, metrics.calc_CustomMetric,
                        metrics.calc_CustomMetric_dsp, metrics.calc_CustomMetric_b)
    metrics.WriteToFile("\Gladiolus_4", metrics.calcContrast, metrics.calc_RMS_Contrast, metrics.calc_CustomMetric,
                        metrics.calc_CustomMetric_dsp, metrics.calc_CustomMetric_b)


if __name__=='__main__':
    funcSign()
    #funcComparasion()