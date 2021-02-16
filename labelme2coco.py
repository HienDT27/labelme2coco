from annotation_utils.labelme.structs import LabelmeAnnotationHandler
from annotation_utils.coco.structs import COCO_Dataset, COCO_Category_Handler

# Path Variables
img_dir = '/home/hien/Desktop/ElectricalDrawing_Kume_san/ElectricalDrawing/112_crop_testdata/hien_all_2/image/'
json_dir = '/home/hien/Desktop/ElectricalDrawing_Kume_san/ElectricalDrawing/112_crop_testdata/hien_all_2/image/'
categories_conf_path = '/home/hien/labelme_test/hien_all_2/hien_all_2_symbol_categories.json'

# Load Labelme Annotation Handler
labelme_handler = LabelmeAnnotationHandler.load_from_dir(load_dir=json_dir)

# Load COCO Dataset from Labelme Annotation Handler
coco_dataset = COCO_Dataset.from_labelme(
    labelme_handler=labelme_handler,
    categories=COCO_Category_Handler.load_from_path(categories_conf_path),
    img_dir=img_dir
)

# Save COCO Dataset to a file
coco_dataset.save_to_path(save_path='/home/hien/Desktop/ElectricalDrawing_Kume_san/ElectricalDrawing/112_crop_testdata/hien_all_2/coco.json', overwrite=True)

# Preview COCO Dataset
coco_dataset.display_preview(show_details=True)
coco_dataset.save_visualization(show_details=True)
# coco_dataset.save_video(show_details=True)