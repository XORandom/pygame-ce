# pure python sources
test_files = files(
    '__init__.py',
    '__main__.py',
    'base_test.py',
    'blit_test.py',
    'bufferproxy_test.py',
    'camera_test.py',
    'color_test.py',
    'constants_test.py',
    'controller_test.py',
    'cursors_test.py',
    'debug_test.py',
    'display_test.py',
    'docs_test.py',
    'draw_test.py',
    'event_test.py',
    'font_test.py',
    'freetype_test.py',
    'ftfont_test.py',
    'geometry_test.py',
    'gfxdraw_test.py',
    'image__save_gl_surface_test.py',
    'image_test.py',
    'imageext_test.py',
    'joystick_test.py',
    'key_test.py',
    'locals_test.py',
    'mask_test.py',
    'math_test.py',
    'midi_test.py',
    'mixer_music_test.py',
    'mixer_test.py',
    'mouse_test.py',
    'pixelarray_test.py',
    'pixelcopy_test.py',
    'rect_test.py',
    'render_test.py',
    'rwobject_test.py',
    'scrap_tags.py',
    'scrap_test.py',
    'sndarray_tags.py',
    'sndarray_test.py',
    'sprite_test.py',
    'surface_test.py',
    'surfarray_tags.py',
    'surfarray_test.py',
    'surflock_test.py',
    'sysfont_test.py',
    'system_test.py',
    'time_test.py',
    'touch_test.py',
    'transform_test.py',
    'typing_test.py',
    'version_test.py',
    'video_test.py',
    'window_test.py',
)

py.install_sources(test_files, subdir: pg / 'tests')

install_subdir('fixtures', install_dir: pg_dir / 'tests', install_tag: 'pg-tag')
subdir('test_utils')
