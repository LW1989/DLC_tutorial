import deeplabcut  
path_config_file = '/home/wallhorn/DLC_Projects/wurm_1-lutz-2023-03-02/config.yaml'
path_to_video=['/home/wallhorn/DLC_Projects/wurm_1-lutz-2023-03-02/videos']

deeplabcut.analyze_videos(path_config_file, path_to_video, videotype='.avi', save_as_csv=True)

