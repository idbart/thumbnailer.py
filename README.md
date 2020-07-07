# thumbnailer.py
## A python script for generating photo thumbnails 

### Usage:

Options:
* -r <rootDirectory>
	* set the directory of original photos
	* if this option is not set, the script will default to the current directory
* -o <outputDirectory> 
	* set the output directory for the generated thumbnails
	* if this option is not set, the script will default to '<rootDirectory>/thumbnails'
	* if the provided directory does not yet exist it will be created automatically
* -w <thumbnailWidth>
	* set the max width for the thumbnails
	* if only a width is provided, the pixel ratio will be maintained and the width will be equal to the provided number 
* -h <thumbnailHeight> 
	* set the max height for the thumbnails
	* if only a height is provided, the pixel ratio will be maintained and the height will be equal to the provided number
	* if the user provides both a width and height, the pixel ratio of the original photo will still be maintained and the dimensions of the thumbnail will not exceed those provided by the user 
