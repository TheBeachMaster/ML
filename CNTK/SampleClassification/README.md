# Classifier Model


<summary> 

### Set up
<details>
Here's how you set up this project : 

### Auto
1. Clone this repo ~(gist should be out soon)~ [This Gist is available](https://gist.github.com/TheBeachMaster/1f9c442e9f25e2470207d560bbfd826f)  

2. On *Windows* open up command prompt and type the following (from your project directory) 
3. Type the following `cntk.exe configFile=ModelClass.cntk makeMode=false` 
4. If you want to do it manually ,ensure you have the `.cntk` file and the Test and Training Data 

## Note: 
That a Folder *ModelOut* will be created during the training session 
  
</details>
</summary>

<summary> 

### Sample Output Images(Milestones)
<details> 

1. Your model will not correctly evaluate 1 out of 9 of the datasets : 
![alt Error][error]  
2. It might take a couple of minutes or hours(on slow PCs)to train the model 
![alt Training][train] 
3. The data dumped in the ModelOut directory should help you fix issues that may result due to an overfit or underfit model 
![alt ModelOut][model] 


[error]:milestones/error.png 
[train]:milestones/firstestrun.png 
[model]:milestones/ml.png
</details>
</summary>