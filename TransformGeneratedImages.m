%before running the code make sure that the original folder (location) is
%copied and pasted and its name is changed as the new folder one
%e.q  copy png_matlab_test and paste it and change its name to png_matlab_test_2
%Location of notes of png ones 
location = 'C:\Users\ONUR\Desktop\matlab\Matlab Project\smc_new\test_last\Sheet-Music-Recognition\generate_database\png_objects_newtrial';

imds = imageDatastore(location, 'IncludeSubfolders', true, 'LabeLSource', 'foldernames');

numberOfImages = length(imds.Files)
for i=1:numberOfImages 
image=readimage(imds,i);
%new location of the appropiate tranformed png's are placed in the new
%folder called png_notes_2
imwrite(repmat(image, 1, 1, 3),replace(imds.Files{i},"png_objects_newtrial","png_objects_newtrial_2"));
%disp(i);
end

%to test them run the code below uncomment it 
%and check the sizes it should be x y 3
new_location = 'C:\Users\ONUR\Desktop\matlab\Matlab Project\smc_new\test2\png_matlab_last_2\';
imds = imageDatastore(new_location, 'IncludeSubfolders', true, 'LabeLSource', 'foldernames');
size(imread(imds.Files{1}))
%before running this part please copy the file and paste it with the new
%folder name pre->pre_matlab
% the seperated and preprocessed directory of the test examples
%for each directory you have for test data, the path needs to be configured
%TODO: recursively files could be taken and being processed
pre_processed = 'C:\Users\ONUR\Desktop\matlab\Matlab Project\smc_new\test2\pre_processed\line_0.png\line_0';

imds_pre_processed = imageDatastore(pre_processed);
% resizes from 100*40 to 100*100 and resizes it to 224,224 to not distort
% image. Also (100-40)=30 0-30 and 70-100 is matrix of ones    31-70 is the
% image. Also note that the image is centered and white spaces are added
% also transformed in 224 224 3
for i=1:length(imds_pre_processed.Files)
new_ing=ones(100,100,1);
tesmp_img=imread(imds_pre_processed.Files{i});
new_ing(:,31:70)=tesmp_img(:,:);
resized_ing=imresize(new_ing,[224,224]);
%the new directory of the files pre_processed_last_matlab
imwrite(repmat(resized_ing, 1, 1, 3),replace(imds_pre_processed.Files{i},"pre_processed","pre_processed_matlab"));
end
new_pre_processed = 'C:\Users\ONUR\Desktop\matlab\Matlab Project\smc_new\test2\pre_processed_matlab\line_0.png\line_0';
imds_pre_processed = imageDatastore(new_pre_processed, 'IncludeSubfolders', true, 'LabeLSource', 'foldernames');
size(imread(imds_pre_processed.Files{1}))









% 
% pre_processed_pattth = 'C:\Users\ONUR\Desktop\matlab\Matlab Project\smc_new\test_last\Sheet-Music-Recognition\object_detection\separated_notes'
% 'C:\Users\ONUR\Desktop\matlab\Matlab Project\smc_new\test_last\Sheet-Music-Recognition\object_detection\separated_notes\Der Mond ist aufgegangen\line_0';
% imds_pre_processed_pattth = imageDatastore(pre_processed_pattth, 'IncludeSubfolders', true, 'LabeLSource', 'foldernames');
% resizes from 100*40 to 100*100 and resizes it to 224,224 to not distort
% image. Also (100-40)=30 0-30 and 70-100 is matrix of ones    31-70 is the
% image. Also note that the image is centered and white spaces are added
% also transformed in 224 224 3
% C:\Users\ONUR\Desktop\matlab\Matlab
% Project\smc_new\test_last\Sheet-Music-Recognition\object_detection\separated_notes\Schlaf Kindlein Schlaf\line_2
% for i=1:length(imds_pre_processed_pattth.Files)
% imds_pre_processed_pattth.Files{i}
% tesmp_img=imread(imds_pre_processed_pattth.Files{i});
% imageSizeHeight=size(tesmp_img,1);
% imageSizeLength=size(tesmp_img,2);
% biggerSide=imageSizeHeight;
% lesserSide=imageSizeLength;
% heightbigger=1;
% if imageSizeLength>imageSizeHeight
% biggerSide=imageSizeLength;
% lesserSide=imageSizeHeight;
% heightbigger=0;
% topside is padded
% else left right
% end
% new_ing=ones(biggerSide,biggerSide,1);
% middle=int32(floor(biggerSide/2));
% if(heightbigger==1)
% if(mod(lesserSide,2)==0)
% new_ing(:,middle-int32(floor( lesserSide/2)):middle+int32(floor( lesserSide/2))-1)=tesmp_img(:,:);
% else
% new_ing(:,middle-int32(floor( lesserSide/2)):middle+int32(floor( lesserSide/2)))=tesmp_img(:,:);
% end
% else
% if(mod(lesserSide,2)==0)
% new_ing(middle-int32(floor( lesserSide/2)):middle+int32(floor( lesserSide/2))-1,:)=tesmp_img(:,:);
% else
% new_ing(middle-int32(floor( lesserSide/2))-1:middle+int32(floor( lesserSide/2))-1,:)=tesmp_img(:,:);
% end
% end
% imshow(new_ing)
% resized_ing=imresize(new_ing,[224,224]);
% the new directory of the files pre_processed_last_matlab
% imwrite(repmat(resized_ing, 1, 1, 3),replace(imds_pre_processed_pattth.Files{i},"separated_notes","separated_notes_2"));
% end
