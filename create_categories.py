from annotation_utils.coco.structs import COCO_Category_Handler, COCO_Category

handler = COCO_Category_Handler()

handler.append(
    COCO_Category.from_label_skeleton(
        supercategory='', # Supercategory Name
        name='bracket_light', # Object Name
        id=len(handler),
        label_skeleton=''
    )
)

handler.save_to_path(save_path='hien_all_2_symbol_categories.json', overwrite=True) # Save Categorie
