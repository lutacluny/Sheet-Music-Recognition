location = '/home/fritz/Informatik/5. Semester/Machine Learning MATLAB/Sheet-Music-Recognition/png_kinds/';

imds = imageDatastore(location, 'IncludeSubfolders', true, 'LabeLSource', 'foldernames');

figure;
perm = randperm(2250,20);
for i = 1:20
    subplot(4,5,i);
    imshow(imds.Files{perm(i)});
end

labelCount = countEachLabel(imds);

img = readimage(imds,1);
img_size = size(img);

numTrainFiles = 2250;
[imdsTrain,imdsValidation] = splitEachLabel(imds,numTrainFiles,'randomize');

layers = [
    imageInputLayer([img_size(1) img_size(2) 1])
    
    convolution2dLayer([10 4],2,'Padding','same')
    batchNormalizationLayer
    reluLayer
    
    maxPooling2dLayer(2,'Stride',2)
    
    convolution2dLayer([10 4],4,'Padding','same')
    batchNormalizationLayer
    reluLayer
    
    maxPooling2dLayer(2,'Stride',2)
    
    convolution2dLayer([10 4], 8,'Padding','same')
    batchNormalizationLayer
    reluLayer
    
    fullyConnectedLayer(5)
    softmaxLayer
    classificationLayer];

options = trainingOptions('sgdm', ...
    'InitialLearnRate',0.005, ...
    'MaxEpochs',2, ...
    'Shuffle','every-epoch', ...
    'ValidationData',imdsValidation, ...
    'ValidationFrequency',30, ...
    'Verbose',false, ...
    'Plots','training-progress');

net = trainNetwork(imdsTrain,layers,options);

YPred = classify(net,imdsValidation);
YValidation = imdsValidation.Labels;
accuracy = sum(YPred == YValidation)/numel(YValidation);

test_location = '/home/fritz/Informatik/5. Semester/Machine Learning MATLAB/Sheet-Music-Recognition/hand_written_notes/pre_processed/';

imds_test = imageDatastore(test_location);
pred_test = classify(net,imds_test);
disp(pred_test)
