from logger import logger
from annotation_utils.ndds.structs import NDDS_Dataset
from annotation_utils.coco.structs import COCO_Dataset, COCO_Category_Handler, COCO_Category

#src_dir = '/home/clayton/workspace/prj/data_keep/data/ndds/TestCapturer_cup'
#dst_dir = 'cup_dataset'
src_dir = '/home/hien/3d/Dataset_Synthesizer/Source/NVCapturedData/TestCapturer'
dst_dir = 'crescent_dataset_val'

# Load NDDS Dataset
ndds_dataset = NDDS_Dataset.load_from_dir(
    json_dir=src_dir,
    show_pbar=True
)

# Fix NDDS Dataset naming so that it follows convention. (This is not necessary if the NDDS dataset already follows the naming convention.)
for frame in ndds_dataset.frames:
    # Fix Naming Convention
    for ann_obj in frame.ndds_ann.objects:
        if ann_obj.class_name.startswith('crescent'):
            obj_type, obj_name = 'seg', 'crescent'
            instance_name = '0'
            ann_obj.class_name = f'{obj_type}_{obj_name}_{instance_name}'

# Convert To COCO Dataset
crescent_categories = COCO_Category_Handler()
crescent_categories.append(
    COCO_Category(
        id=len(crescent_categories),
        name='crescent'
    )
)
dataset = COCO_Dataset.from_ndds(
    ndds_dataset=ndds_dataset,
    categories=crescent_categories,
    naming_rule='type_object_instance_contained',
    show_pbar=True,
    bbox_area_threshold=-1,
    allow_unfound_seg=True
)
dataset.move_images(
    dst_img_dir=dst_dir,
    preserve_filenames=True,
    overwrite_duplicates=False,
    update_img_paths=True,
    overwrite=True,
    show_pbar=True
)
dataset.save_to_path(f'{dst_dir}/output.json', overwrite=True)
# dataset.display_preview(show_details=True)
dataset.save_video(
    save_path=f'{dst_dir}/preview.mp4',
    fps=5,
    show_details=True
)