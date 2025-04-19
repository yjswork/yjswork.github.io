import os
import re

# Path to your wav/image directory
demo_dir = '/home/jeonyj0612/yjswork.github.io/demos/Project9-MultiModal-F2S-v2/static/wavs/forDemo'
output_html = '/home/jeonyj0612/yjswork.github.io/demos/Project9-MultiModal-F2S-v2/index.html'

# Collect all IDs based on existing GT audio
pattern = re.compile(r'gt-(\d+)\.wav')
ids = sorted([
    pattern.match(f).group(1)
    for f in os.listdir(demo_dir)
    if pattern.match(f)
], key=lambda x: int(x))

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

for i, id in enumerate(ids):
    part1_section += f'''
    <div class="columns is-centered">
      <div class="column is-four-fifths has-text-right">
        <h4 class="title is-4">Part 1 - Case {i+1}</h4>
      </div>
    </div>
    <div class="columns is-centered has-text-centered">
      <div class="column is-four-fifths">
        <div class="content">
          <p><b>Ground Truth</b></p>
          <audio controls>
            <source src="forDemo/gt-{id}.wav" type="audio/wav">
          </audio>
        </div><br>
        <div class="columns is-centered">
          <div class="column content has-text-centered">
            <p><b>Model-A</b></p>
            <audio controls><source src="forDemo/pluster-{id}.wav" type="audio/wav"></audio>
          </div>
          <div class="column content has-text-centered">
            <p><b>Model-B</b></p>
            <audio controls><source src="forDemo/FaceTTS-{id}.wav" type="audio/wav"></audio>
          </div>
          <div class="column content has-text-centered">
            <p><b>Model-C</b></p>
            <audio controls><source src="forDemo/FVTTS-{id}.wav" type="audio/wav"></audio>
          </div>
          <div class="column content has-text-centered">
            <p><b>Model-D</b></p>
            <audio controls><source src="forDemo/proposed-{id}.wav" type="audio/wav"></audio>
          </div>
        </div>
      </div>
    </div><br><br>
    '''

    part2_section += f'''
    <div class="columns is-centered">
      <div class="column is-four-fifths has-text-right">
        <h4 class="title is-4">Part 2 - Case {i+1}</h4>
      </div>
    </div>
    <div class="columns is-centered has-text-centered">
      <div class="column is-four-fifths">
        <div class="content">
          <p><b>Ground Truth Image</b></p>
          <img src="forDemo/image-{id}.jpg" width="200">
        </div><br>
        <div class="columns is-centered">
          <div class="column content has-text-centered">
            <p><b>Model-A</b></p>
            <audio controls><source src="forDemo/pluster-{id}.wav" type="audio/wav"></audio>
          </div>
          <div class="column content has-text-centered">
            <p><b>Model-B</b></p>
            <audio controls><source src="forDemo/FaceTTS-{id}.wav" type="audio/wav"></audio>
          </div>
          <div class="column content has-text-centered">
            <p><b>Model-C</b></p>
            <audio controls><source src="forDemo/FVTTS-{id}.wav" type="audio/wav"></audio>
          </div>
          <div class="column content has-text-centered">
            <p><b>Model-D</b></p>
            <audio controls><source src="forDemo/proposed-{id}.wav" type="audio/wav"></audio>
          </div>
        </div>
      </div>
    </div><br><br>
    '''

with open(output_html, 'w') as f:
    f.write(html_head + part1_section + part2_section + html_tail)

print(f"HTML file '{output_html}' generated with {len(ids)} cases.")
