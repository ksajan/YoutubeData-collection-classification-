<?php
  $api_key = 'AIzaSyAmmVvu2Zl3iu-2k2CTiDuaI5gP7OLrmqc';
  
  $video_url = 'https://www.youtube.com/watch?v=1ejTKov_Sm4';
  
  $api_url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id=' . getYouTubeVideoID($video_url) . '&key=' . $api_key;
        
  $data = json_decode(file_get_contents($api_url));
  
  // Accessing Video Info
  echo '<strong>Title: </strong>' . $data->items[0]->snippet->title . '<br>';
  echo '<strong>publishedAt: </strong>' . $data->items[0]->snippet->publishedAt . '<br>';
  echo '<strong>Duration: </strong>' . $data->items[0]->contentDetails->duration . '<br>';
  echo '<strong>Duration: </strong>' . $data->items[0]->statistics->viewCount . '<br>';
  
?>