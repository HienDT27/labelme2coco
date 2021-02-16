from annotation_utils.labelme.structs import LabelmeAnnotationHandler
from annotation_utils.coco.structs import COCO_Dataset, COCO_Category_Handler

# Path Variables
img_dir = ''
json_dir = ''
categories_conf_path = ''

# Load Labelme Annotation Handler
labelme_handler = LabelmeAnnotationHandler.load_from_dir(load_dir=json_dir)

# Load COCO Dataset from Labelme Annotation Handler
coco_dataset = COCO_Dataset.from_labelme(
    labelme_handler=labelme_handler,
    categories=COCO_Category_Handler.load_from_path(categories_conf_path),
    img_dir=img_dir
)

# Save COCO Dataset to a file
coco_dataset.save_to_path(save_path='', overwrite=True)

# Preview COCO Dataset
coco_dataset.display_preview(show_details=True)
coco_dataset.save_visualization(show_details=True)
# coco_dataset.save_video(show_details=True)
