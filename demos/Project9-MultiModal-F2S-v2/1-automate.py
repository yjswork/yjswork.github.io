import os
import re

# Define input list of IDs to include
ids = ['2', '3', '4', '5', '9', '10', '13', '14', '15', '16', '18', '20', '21', '26', '29', '30', '35', '37', '38', '44', '47', '62', '69', '101','102', '103', '105', '107','108', '110', '111', '113','114', '115', '116', '118','119', '121', '122', '124']  # example list you can customize
print(len(ids))

# Define paths for each model and ground truth
pluster_dir = '/home/jeonyj0612/yjswork.github.io/demos/Project9-MultiModal-F2S-v2/static/wavs/1-pluster-baseline-350000'
facetts_dir = '/home/jeonyj0612/yjswork.github.io/demos/Project9-MultiModal-F2S-v2/static/wavs/1-facetts-naver'
fvtts_dir = '/home/jeonyj0612/yjswork.github.io/demos/Project9-MultiModal-F2S-v2/static/wavs/1-fvtts-interspeech2024'
proposed_dir = '/home/jeonyj0612/yjswork.github.io/demos/Project9-MultiModal-F2S-v2/static/wavs/3-6-DoubleClassifier-2attGenderRace-0.3-350000'
gt_audio_dir = '/home/jeonyj0612/yjswork.github.io/demos/Project9-MultiModal-F2S-v2/static/wavs/0-gt_audio'
gt_image_dir = '/home/jeonyj0612/yjswork.github.io/demos/Project9-MultiModal-F2S-v2/static/wavs/0-gt_images'

output_html = '/home/jeonyj0612/yjswork.github.io/demos/Project9-MultiModal-F2S-v2/index.html'

html_head = '''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="description" content="FaceSpeech">
  <meta name="keywords" content="multi-modality">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Demo</title>

  <link href="https://fonts.googleapis.com/css?family=Google+Sans|Noto+Sans|Castoro" rel="stylesheet">
  <link rel="stylesheet" href="./static/css/bulma.min.css">
  <link rel="stylesheet" href="./static/css/index.css">
</head>
<body>
<section class="section">
  <div class="container is-max-desktop">
    <div class="columns is-centered has-text-centered">
      <div class="column is-four-fifths">
        <h2 class="title is-3">Demo</h2>
      </div>
    </div>
'''

html_tail = '''
  </div>
</section>
</body>
</html>'''

part1_section = ''
part2_section = ''

def find_file_with_id(directory, id):
    pattern = re.compile(rf'^{id}(?:_.*)?\.wav$')
    for f in os.listdir(directory):
        if pattern.match(f):
            return f
    print(f"[Warning] ID {id} not found in {directory}")
    return None

def find_image_file(directory, id, extension):
    for f in os.listdir(directory):
        if re.match(fr'.*{id}(?:_|-)?.*\.{extension}$', f):
            return f
    return None


for i, id in enumerate(ids):
    gt_audio = find_file_with_id(gt_audio_dir, id)
    pluster_audio = find_file_with_id(pluster_dir, id)
    facetts_audio = find_file_with_id(facetts_dir, id)
    fvtts_audio = find_file_with_id(fvtts_dir, id)
    proposed_audio = find_file_with_id(proposed_dir, id)
    gt_image = find_image_file(gt_image_dir, id, 'jpg')

    part1_section += f'''
    <div class="columns is-centered">
      <div class="column is-four-fifths has-text-centered">
        <h4 class="title is-4">Part 1 - Case {i+1}</h4>
      </div>
    </div>
    <div class="columns is-centered has-text-centered">
      <div class="column is-four-fifths">
        <div class="content">
          <p><b>Ground Truth</b></p>
          <audio controls>
            <source src="{gt_audio_dir}/{gt_audio}" type="audio/wav">
          </audio>
        </div><br>
        <div class="columns is-centered">
          <div class="column content has-text-centered">
            <p><b>Model-A</b></p>
            <audio controls><source src="{pluster_dir}/{pluster_audio}" type="audio/wav"></audio>
          </div>
          <div class="column content has-text-centered">
            <p><b>Model-B</b></p>
            <audio controls><source src="{facetts_dir}/{facetts_audio}" type="audio/wav"></audio>
          </div>
          <div class="column content has-text-centered">
            <p><b>Model-C</b></p>
            <audio controls><source src="{fvtts_dir}/{fvtts_audio}" type="audio/wav"></audio>
          </div>
          <div class="column content has-text-centered">
            <p><b>Model-D</b></p>
            <audio controls><source src="{proposed_dir}/{proposed_audio}" type="audio/wav"></audio>
          </div>
        </div>
      </div>
    </div><br><br>
    '''

    part2_section += f'''
    <div class="columns is-centered">
      <div class="column is-four-fifths has-text-centered">
        <h4 class="title is-4">Part 2 - Case {i+1}</h4>
      </div>
    </div>
    <div class="columns is-centered has-text-centered">
      <div class="column is-four-fifths">
        <div class="content">
          <p><b>Ground Truth Image</b></p>
          <img src="{gt_image_dir}/{gt_image}" width="200">
        </div><br>
        <div class="columns is-centered">
          <div class="column content has-text-centered">
            <p><b>Model-A</b></p>
            <audio controls><source src="{pluster_dir}/{pluster_audio}" type="audio/wav"></audio>
          </div>
          <div class="column content has-text-centered">
            <p><b>Model-B</b></p>
            <audio controls><source src="{facetts_dir}/{facetts_audio}" type="audio/wav"></audio>
          </div>
          <div class="column content has-text-centered">
            <p><b>Model-C</b></p>
            <audio controls><source src="{fvtts_dir}/{fvtts_audio}" type="audio/wav"></audio>
          </div>
          <div class="column content has-text-centered">
            <p><b>Model-D</b></p>
            <audio controls><source src="{proposed_dir}/{proposed_audio}" type="audio/wav"></audio>
          </div>
        </div>
      </div>
    </div><br><br>
    '''

with open(output_html, 'w') as f:
    f.write(html_head + part1_section + part2_section + html_tail)

print(f"HTML file '{output_html}' generated with {len(ids)} cases.")
