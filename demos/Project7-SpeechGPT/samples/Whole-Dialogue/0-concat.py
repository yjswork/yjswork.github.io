import wave

# infiles = ["Baseline-noHistory/D59/0_0_d59.wav", "Baseline-noHistory/D59/1_1_d59.wav", "Baseline-noHistory/D59/2_0_d59.wav", "Baseline-noHistory/D59/3_1_d59.wav", "Baseline-noHistory/D59/4_0_d59.wav", "Baseline-noHistory/D59/5_1_d59.wav", "Baseline-noHistory/D59/6_0_d59.wav", "Baseline-noHistory/D59/7_1_d59.wav"]
# outfile = "Baseline-noHistory/D59-Baseline-noHistory-all.wav"

# infiles = ["Baseline-noHistory/D64/0_0_d64.wav", "Baseline-noHistory/D64/1_1_d64.wav", "Baseline-noHistory/D64/2_0_d64.wav", "Baseline-noHistory/D64/3_1_d64.wav", "Baseline-noHistory/D64/4_0_d64.wav", "Baseline-noHistory/D64/5_1_d64.wav", "Baseline-noHistory/D64/6_0_d64.wav", "Baseline-noHistory/D64/7_1_d64.wav", "Baseline-noHistory/D64/8_0_d64.wav", "Baseline-noHistory/D64/9_1_d64.wav", "Baseline-noHistory/D64/10_0_d64.wav", "Baseline-noHistory/D64/11_1_d64.wav", "Baseline-noHistory/D64/12_0_d64.wav", "Baseline-noHistory/D64/13_1_d64.wav"]
# outfile = "Baseline-noHistory/D64-Baseline-noHistory-all.wav"

# infiles = ["Baseline-noHistory/D71/0_1_d71.wav", "Baseline-noHistory/D71/1_0_d71.wav", "Baseline-noHistory/D71/2_1_d71.wav", "Baseline-noHistory/D71/3_0_d71.wav", "Baseline-noHistory/D71/4_1_d71.wav", "Baseline-noHistory/D71/5_0_d71.wav"]
# outfile = "Baseline-noHistory/D71-Baseline-noHistory-all.wav"

infiles = ["Baseline-noHistory/D79/0_1_d79.wav", "Baseline-noHistory/D79/1_0_d79.wav", "Baseline-noHistory/D79/2_1_d79.wav", "Baseline-noHistory/D79/3_0_d79.wav", "Baseline-noHistory/D79/4_1_d79.wav", "Baseline-noHistory/D79/5_0_d79.wav", "Baseline-noHistory/D79/6_1_d79.wav", "Baseline-noHistory/D79/7_0_d79.wav", "Baseline-noHistory/D79/8_1_d79.wav", "Baseline-noHistory/D79/9_0_d79.wav", "Baseline-noHistory/D79/10_1_d79.wav", "Baseline-noHistory/D79/11_0_d79.wav", "Baseline-noHistory/D79/12_1_d79.wav"]
outfile = "Baseline-noHistory/D79-Baseline-noHistory-all.wav"

data= []
for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()
    
output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
for i in range(len(data)):
    output.writeframes(data[i][1])
output.close()