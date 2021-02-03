clear; close all; clc
%location of resized training images .png
location = 'C:\Users\ONUR\Desktop\matlab\Matlab Project\smc_new\test2\png_notes_2\';
imds = imageDatastore(location, 'IncludeSubfolders', true, 'LabeLSource', 'foldernames');
%location of the resized test preprocessed images 
test_location_matlab = 'C:\Users\ONUR\Desktop\matlab\Matlab Project\smc_new\test2\pre_processed_matlab\line_2.png\line_2\';
imds_test = imageDatastore(test_location_matlab);
perm = randperm(2250,20);
% for i = 1:20
%     subplot(4,5,i);
%     imshow(imds.Files{perm(i)});
% end


labelCount = countEachLabel(imds);

img = readimage(imds,1);
img_size = size(img);

%numTrainFiles = 2250;
%split training validation  test 0.6 0.2 0.2
%real test data is different -> those are for the generated ones
[imdsTrain,imdsValidation,imdsTest] = splitEachLabel(imds,0.6,0.2,'randomize');


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


net=googlenet;
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
    'MaxEpochs',5, ...
    'Shuffle','every-epoch', ...
    'ValidationData',imdsValidation, ...
    'ValidationFrequency',30, ...
    'Verbose',false, ...
    'Plots','training-progress',...,
'ExecutionEnvironment','gpu');


net = trainNetwork(imdsTrain,lgraph,options);


YPred = classify(net,imdsValidation);
YValidation = imdsValidation.Labels;
accuracy = sum(YPred == YValidation)/numel(YValidation);


pred_test = classify(net,imdsTest);
test_Acc=sum(pred_test == imdsTest.Labels)/size(pred_test,1);

realTest_Res= classify(net,imds_test);


