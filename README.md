# Sheet-Music-Recognition

## Generate the data set 
In 'generate_dataset' execute the following scripts in the given order. The data set contains the respective png images of the musical notation and can be found in 'generate_dataset/png_objects'.

1. generate_svg_notes_with_rotation.py
2. generate_svg_notes_grouped_with_rotation.py
3. generate_svg_symbols_with_rotation.py
4. convert_svg_to_png.py
 
## Detect the objects 

In 'object_detection' execute the following scripts in the given order. The output can be found in 'object_detection/separated_notes'. There is on directory for each tune containing its rows as subdirectories. 

1. identify_lines.py
2. separate_notes.py
3. identify_groups_of_notes.py
4. separate_groups_of_notes.py

## Classify the objects 
There are parameters that can be controlled. idms locations: training data location
net(resnet50/googlenet) net to be trained
diroutput: location of outputs of notes
dirtest: location of object detection(seperated notes)
## Convert to audio file 
n 'process_output' execute the following script. The audio files can be accessed in 'process_output/audios'

1. output_to_wav.py

## Get the results
In 'process_output' execute the following script. It will compare each label to the ground truth given in 'process_output\label_files' and print the result to the console. 

1. compare_labels.py
