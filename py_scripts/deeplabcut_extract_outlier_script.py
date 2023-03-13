# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:05:14 2022

@author: Lutz
"""
import deeplabcut
ProjectFolderName = 'top_view_test_1-Wallhorn-2022-01-13'
VideoType = '.mp4'
videofile_path = ['/home/wallhorn/DLC_Projects/top_view_test_1-Wallhorn-2022-01-13/new_videos/bl6_inhibition_trimmed']
destfolder='/home/wallhorn/DLC_Projects/'+ProjectFolderName+'/video/videos_bremen/ir_test/new_labels'
path_config_file = '/home/wallhorn/DLC_Projects/'+ProjectFolderName+'/config.yaml'

deeplabcut.extract_outlier_frames(path_config_file, videofile_path,videotype=VideoType, outlieralgorithm='fitting', p_bound=0.01, epsilon=10, extractionalgorithm='kmeans')
