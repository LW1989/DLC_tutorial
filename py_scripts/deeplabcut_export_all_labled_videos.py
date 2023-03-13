import deeplabcut  

path_config_file = '/home/wallhorn/DLC_Projects/top_view_08_2022-Wallhorn-2022-08-11/config.yaml'
path_to_video=['/home/wallhorn/DLC_Projects/top_view_08_2022-Wallhorn-2022-08-11/nex_bl6_project/videos/bl6_epm_naive_2263_trimmed.mp4']

deeplabcut.create_labeled_video(path_config_file, path_to_video, videotype='.mp4', draw_skeleton = True)
