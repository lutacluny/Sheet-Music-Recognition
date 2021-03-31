clear; close all; clc
%location of resized training images .png

location = 'C:\Users\ONUR\Desktop\matlab\Matlab Project\smc_new\test_last\Sheet-Music-Recognition\generate_database\png_objects_new_2\';
imds = imageDatastore(location, 'IncludeSubfolders', true, 'LabeLSource', 'foldernames');
%location of the resized test preprocessed images 
%C:\Users\ONUR\Desktop\matlab\Matlab Project\smc_new\test_last\Sheet-Music-Recognition\object_detection\separated_notes
test_location_matlab = 'C:\Users\ONUR\Desktop\matlab\Matlab Project\smc_new\test_last\Sheet-Music-Recognition\object_detection\separated_notes\Der Mond ist aufgegangen\line_0';
imds_test = imageDatastore(test_location_matlab);
imds_test.Files
perm = randperm(2250,20);
% for i = 1:20
%     subplot(4,5,i);
%     imshow(imds.Files{perm(i)});
% end

test_location_matlab_last = 'C:\Users\ONUR\Desktop\matlab\Matlab Project\smc_new\test_last\Sheet-Music-Recognition\object_detection\separated_notes\';
%
%
%
%
labelCount = countEachLabel(imds);

img = readimage(imds,1);
img_size = size(img);

%numTrainFiles = 2250;
%split training validation  test 0.6 0.2 0.2
%real test data is different -> those are for the generated ones
[imdsTrain,imdsValidation,imdsTest] = splitEachLabel(imds,0.6,0.2');


% layers = [
%     imageInputLayer([img_size(1) img_size(2) 1])
%     
%     convolution2dLayer([10 4],2,'Padding','same')
%     batchNormalizationLayer
%     reluLayer
%     
%     maxPooling2dLayer(2,'Stride',2)
%     
%     convolution2dLayer([10 4],4,'Padding','same')
%     batchNormalizationLayer
%     reluLayer
%     
%     maxPooling2dLayer(2,'Stride',2)
%     
%     convolution2dLayer([10 4], 8,'Padding','same')
%     batchNormalizationLayer
%     reluLayer
%     
%     fullyConnectedLayer(39)
%     softmaxLayer
%     classificationLayer];
% 


net=resnet50;
%net=googlenet;

if isa(net,'SeriesNetwork') 
  lgraph = layerGraph(net.Layers); 
else
  lgraph = layerGraph(net);
end 
[learnableLayer,classLayer] = findLayersToReplace(lgraph);
numClasses = numel(categories(imdsTrain.Labels));
if isa(learnableLayer,'nnet.cnn.layer.FullyConnectedLayer')
    newLearnableLayer = fullyConnectedLayer(numClasses, ...
        'Name','new_fc', ...
        'WeightLearnRateFactor',10, ...
        'BiasLearnRateFactor',10);
    
elseif isa(learnableLayer,'nnet.cnn.layer.Convolution2DLayer')
    newLearnableLayer = convolution2dLayer(1,numClasses, ...
        'Name','new_conv', ...
        'WeightLearnRateFactor',10, ...
        'BiasLearnRateFactor',10);
end

lgraph = replaceLayer(lgraph,learnableLayer.Name,newLearnableLayer);
newClassLayer = classificationLayer('Name','new_classoutput');
lgraph = replaceLayer(lgraph,classLayer.Name,newClassLayer);
layers = lgraph.Layers;
connections = lgraph.Connections;

layers(1:10) = freezeWeights(layers(1:10));
lgraph = createLgraphUsingConnections(layers,connections);

options = trainingOptions('sgdm', ...
    'InitialLearnRate',0.005, ...
    'MaxEpochs',3, ...
    'Shuffle','every-epoch', ...
    'ValidationData',imdsValidation,...
    'ValidationFrequency',30, ...
    'Verbose',false, ...
    'Plots','training-progress',...,
    'MiniBatchSize',32, ...
'ExecutionEnvironment','gpu');

    

net = trainNetwork(imds,lgraph,options);
% i=1;
% imshow(imds_test_location_matlab_last.Files{i});
% classify(net,imread(imds_test_location_matlab_last.Files{i}))
 YPred = classify(net,imdsValidation);
YValidation = imdsValidation.Labels;
accuracy = sum(YPred == YValidation)/numel(YValidation);


pred_test = classify(net,imdsTest);
test_Acc=sum(pred_test == imdsTest.Labels)/size(pred_test,1);
mapObj = containers.Map({'Der Mond ist aufgegangen','Fuchs du hast die Gans gestohlen', 'Schlaf Kindlein Schlaf','Schlaf Main Kinderl Schlaf','Simple Melody','Speed the Plough','Spottlied auf den 1574 aus Krakau entflohenen Polenkoenig','Wilhelmus von Nassouwe'}, {1, 2,3,4,5,6,7,8});

TesterVariable = [];
%('name',"",'real',[],"predicted",[]);
dirtest='C:\Users\ONUR\Desktop\matlab\Matlab Project\smc_new\test_last\Sheet-Music-Recognition\object_detection\separated_notes_2'

imds_test_location_matlab_last_simple = imageDatastore('C:\Users\ONUR\Desktop\matlab\Matlab Project\smc_new\test_last\Sheet-Music-Recognition\object_detection\separated_notes_2\Simple Melody\line_0\', 'IncludeSubfolders',true,'FileExtensions',{'.png'})
imds_test_location_matlab_last = imageDatastore(dirtest, 'IncludeSubfolders',true,'FileExtensions',{'.png'})
listing = dir(dirtest);
EvalArr={};
diroutput='C:\Users\ONUR\Desktop\matlab\Matlab Project\smc_new\test_last\Sheet-Music-Recognition\process_output\output_label_files\'
for j=3:size(listing,1)
    songName=listing(j).name;
    listingFileLine = dir(dirtest+"\"+songName);
    target=diroutput+convertCharsToStrings(songName);
    fid = fopen(target,'wt');
   
for li=3:size(listingFileLine,1)
    lineStr=listingFileLine(li).name;
    listingFileNotes = dir(dirtest+"\"+songName+"\"+lineStr);
    imds_test_line = imageDatastore(dirtest+"\"+songName+"\"+lineStr,'FileExtensions',{'.png'});
    pred=strings([size(imds_test_line.Files,1),1]);
    lineRes= classify(net,imds_test_line);
    Rescells=cellstr(lineRes);
    for i=1:size(imds_test_line.Files,1) 
    TestClass=split(imds_test_line.Files{i},"\separated_notes_2\");
    TestCass=split(TestClass(2),"\line_");
    lineNo=TestCass(2);
    lineNo=split(lineNo,"\note");
    lineNo=lineNo(1);
    TestClass=TestCass(1);
    splitted=split(imds_test_line.Files{i},"note_");
    splitted=split(splitted(2),".");
     index=str2num(splitted{1})+1;
    pred(index)= Rescells{i};
        
    end
%      imds_test_line.Files
%      lineRes
%      Rescells
%      pred
%     
    for jl=1:size(pred,1)
        
         fprintf(fid,replace(replace(pred(jl),"_top",""),"_bottom","")+" ");
    end
             fprintf(fid,"\n");

end
    fclose(fid);

  % EvalArr{mapObj(listing(i).name)}=struct("name",listing(i).name);
end
listingGroundTruth = dir(dirtest);

lolo=13;
realTest_Res(lolo,:)
imds_test_location_matlab_last_simple.Files(lolo)
realTest_Resacc(lolo)
[realTest_Resacc,realTest_Res]= classify(net,imds_test_location_matlab_last_simple);


pred=strings([size(imds_test_location_matlab_last.Files,1),1]);
for i=1:size(imds_test_location_matlab_last.Files,1) 
    TestClass=split(imds_test_location_matlab_last.Files{i},"\separated_notes_2\");
    TestCass=split(TestClass(2),"\line_");
    lineNo=TestCass(2);
    lineNo=split(lineNo,"\note");
    lineNo=lineNo(1);
    
    TestClass=TestCass(1);
    splitted=split(imds_test_location_matlab_last.Files{i},"note_");
    splitted=split(splitted(2),".")
  index=str2num(splitted{1})+1;
 cells=cellstr(realTest_Resacc);
 pred(index)= cells{index};
     disp("Song:" +TestClass+"   Line No:"+lineNo + "     Index="+index );
EvalArr{mapObj(TestClass)}
end
