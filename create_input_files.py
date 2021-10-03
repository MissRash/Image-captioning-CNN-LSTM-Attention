from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='flickr8k',
                       karpathy_json_path='/content/drive/MyDrive/a-PyTorch-Tutorial-to-Image-Captioning/caption_datasets/dataset_flickr8k.json',
                       image_folder='/content/drive/MyDrive/images/Flicker8k_Dataset',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='/content/drive/MyDrive/a-PyTorch-Tutorial-to-Image-Captioning/output',
                       max_len=50)
