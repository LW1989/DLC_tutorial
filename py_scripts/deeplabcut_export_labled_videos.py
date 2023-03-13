import deeplabcut  
ProjectFolderName = 'top_view_test_1-Wallhorn-2022-01-13'
VideoType = 'mpg' 
videofile_path = ['/home/wallhorn/DLC_Projects/'+ProjectFolderName+'/videos/']
path_config_file = '/home/wallhorn/DLC_Projects/'+ProjectFolderName+'/config.yaml'
path_to_video=['/home/wallhorn/DLC_Projects/top_view_test_1-Wallhorn-2022-01-13/videos/OF_Trial_17.mpg']

deeplabcut.create_labeled_video(path_config_file, path_to_video, videotype='.mpg', save_frames=True, draw_skeleton = True)