bl_info = {
    "name": "yup gltf exporter",
    "author": "ousttrue",
    "version": (0, 1),
    "blender": (2, 79, 0),
    "location": "File > Export > yup gltf-2.0(.glb)",
    "description": "yup gltf exporter",
    "warning": "",
    "support": "COMMUNITY",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"
}


import bpy
from bpy.props import BoolProperty
from bpy.props import EnumProperty
from bpy.props import StringProperty


class ExportYUP(bpy.types.Operator):
    """Export selection to YUP"""

    bl_idname = "export_scene.yup"
    bl_label = "Export YUP GLTF"

    filepath = StringProperty(subtype='FILE_PATH')

    # Export options

    SelectedOnly = BoolProperty(
        name="Export Selected Objects Only",
        description="Export only selected objects",
        default=True)

    def execute(self, context):
        self.filepath = bpy.path.ensure_ext(self.filepath, ".glb")
        from . import yup
        yup.export(self.filepath)
        return {'FINISHED'}

    def invoke(self, context, event):
        if not self.filepath:
            self.filepath = bpy.path.ensure_ext(bpy.data.filepath, ".glb")
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


def menu_func(self, context):
    self.layout.operator(ExportYUP.bl_idname, text="YUP GLTF (.glb)")


def register():
    bpy.utils.register_module(__name__)

    bpy.types.INFO_MT_file_export.append(menu_func)


def unregister():
    bpy.utils.unregister_module(__name__)

    bpy.types.INFO_MT_file_export.remove(menu_func)


if __name__ == "__main__":
    register()