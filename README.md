# Machine learning analyse of Human Activity Recognition (HAR)

### What's included

Within the download you'll find the following directories and files:
```
har/
├── data/
│   ├── clean_testing_data.csv
│   ├── clean_training_data.csv
│   └── HAR_data.zip
│        ├── HAR_training.csv
│        └── HAR_testing.csv
├── img/
│   ├── Confusion_Matrix_adelmo.png
│   ├── Confusion_Matrix_carlitos.png
│   ├── Confusion_Matrix_charles.png
│   ├── Confusion_Matrix_eurico.png
│   ├── Confusion_Matrix_jeremy.png
│   ├── Confusion_Matrix_pedro.png
│   ├── Variable_Importance_adelmo.png
│   ├── Variable_Importance_carlitos.png
│   ├── Variable_Importance_charles.png
│   ├── Variable_Importance_eurico.png
│   ├── Variable_Importance_jeremy.png
│   └── Variable_Importance_pedro.png
│
├── assignment.py
├── cleaning_data.py
└── plot_visualization.py
```
***

If you have a clean data, you don't have to first run script `cleaning_data.py`
### Usage:
```
    andrew@zeus:~/projects/python/har$ ipython assignment.py
```

## Results

<div style="margin: 0px auto;">
	<table>
		<tr>
			<th align="center" colspan="3">carlitos</th>
		</tr>
		<tr valign="middle">
			<td align="center">
				<table width="100%">
					<tr>
						<th>id</th>
						<th>class</th>
					</tr>
					<tr>
						<td>9</td>
						<td>A</td>
					</tr>
					<tr>
						<td>11</td>
						<td>B</td>
					</tr>
					<tr>
						<td>18</td>
						<td>B</td>
					</tr>
				</table>
				<br>
				MSE = 0.03854
			</td>
			<td align="center"><img src="https://raw.github.com/ondrej-tucek/Machine-Learning-HAR/master/img/Variable_Importance_carlitos.png" height="300">
			</td>
			<td align="center"><img src="https://raw.github.com/ondrej-tucek/Machine-Learning-HAR/master/img/Confusion_Matrix_carlitos.png" height="300">
			</td>
		</tr>
	</table>
	<table>
		<tr>
			<th align="center" colspan="3">pedro</th>
		</tr>
		<tr valign="middle">
			<td align="center">
				<table width="100%">
					<tr>
						<th>id</th>
						<th>class</th>
					</tr>
					<tr>
						<td>1</td>
						<td>B</td>
					</tr>
					<tr>
						<td>17</td>
						<td>A</td>
					</tr>
					<tr>
						<td>19</td>
						<td>B</td>
					</tr>
				</table>
				<br>
				MSE = 0.03321
			</td>
			<td align="center"><img src="https://raw.github.com/ondrej-tucek/Machine-Learning-HAR/master/img/Variable_Importance_pedro.png" height="300">
			</td>
			<td align="center"><img src="https://raw.github.com/ondrej-tucek/Machine-Learning-HAR/master/img/Confusion_Matrix_pedro.png" height="300">
			</td>
		</tr>
	</table>
	<table>
		<tr>
			<th align="center" colspan="3">adelmo</th>
		</tr>
		<tr valign="middle">
			<td align="center">
				<table width="100%">
					<tr>
						<th>id</th>
						<th>class</th>
					</tr>
					<tr>
						<td>4</td>
						<td>A</td>
					</tr>
				</table>
				<br>
				MSE = 0.01969
			</td>
			<td align="center"><img src="https://raw.github.com/ondrej-tucek/Machine-Learning-HAR/master/img/Variable_Importance_adelmo.png" height="300">
			</td>
			<td align="center"><img src="https://raw.github.com/ondrej-tucek/Machine-Learning-HAR/master/img/Confusion_Matrix_adelmo.png" height="300">
			</td>
		</tr>
	</table>
	<table>
		<tr>
			<th align="center" colspan="3">charles</th>
		</tr>
		<tr valign="middle">
			<td align="center">
				<table width="100%">
					<tr>
						<th>id</th>
						<th>class</th>
					</tr>
					<tr>
						<td>10</td>
						<td>A</td>
					</tr>
				</table>
				<br>
				MSE = 0.00754
			</td>
			<td align="center"><img src="https://raw.github.com/ondrej-tucek/Machine-Learning-HAR/master/img/Variable_Importance_charles.png" height="300">
			</td>
			<td align="center"><img src="https://raw.github.com/ondrej-tucek/Machine-Learning-HAR/master/img/Confusion_Matrix_charles.png" height="300">
			</td>
		</tr>
	</table>
	<table>
		<tr>
			<th align="center" colspan="3">eurice</th>
		</tr>
		<tr valign="middle">
			<td align="center">
				<table width="100%">
					<tr>
						<th>id</th>
						<th>class</th>
					</tr>
					<tr>
						<td>5</td>
						<td>A</td>
					</tr>
					<tr>
						<td>13</td>
						<td>B</td>
					</tr>
					<tr>
						<td>16</td>
						<td>E</td>
					</tr>
					<tr>
						<td>20</td>
						<td>B</td>
					</tr>
				</table>
				<br>
				MSE = 0.03148
			</td>
			<td align="center"><img src="https://raw.github.com/ondrej-tucek/Machine-Learning-HAR/master/img/Variable_Importance_eurico.png" height="300">
			</td>
			<td align="center"><img src="https://raw.github.com/ondrej-tucek/Machine-Learning-HAR/master/img/Confusion_Matrix_eurice.png" height="300">
			</td>
		</tr>
	</table>
	<table>
		<tr>
			<th align="center" colspan="3">jeremy</th>
		</tr>
		<tr valign="middle">
			<td align="center">
				<table width="100%">
					<tr>
						<th>id</th>
						<th>class</th>
					</tr>
					<tr>
						<td>2</td>
						<td>A</td>
					</tr>
					<tr>
						<td>3</td>
						<td>B</td>
					</tr>
					<tr>
						<td>6</td>
						<td>E</td>
					</tr>
					<tr>
						<td>7</td>
						<td>D</td>
					</tr>
					<tr>
						<td>8</td>
						<td>B</td>
					</tr>
					<tr>
						<td>12</td>
						<td>C</td>
					</tr>
					<tr>
						<td>14</td>
						<td>A</td>
					</tr>
					<tr>
						<td>15</td>
						<td>E</td>
					</tr>
				</table>
				<br>
				MSE = 0.02644
			</td>
			<td align="center"><img src="https://raw.github.com/ondrej-tucek/Machine-Learning-HAR/master/img/Variable_Importance_jeremy.png" height="300">
			</td>
			<td align="center"><img src="https://raw.github.com/ondrej-tucek/Machine-Learning-HAR/master/img/Confusion_Matrix_jeremy.png" height="300">
			</td>
		</tr>
	</table>
</div>


## Requirements

- Python 2.7+
- [numpy](http://www.numpy.org/), 1.8.2
- [pandas](http://pandas.pydata.org/), 0.17.1
- [scikit-learn](http://scikit-learn.org/stable/), 0.17
- [matplotlib](http://matplotlib.org/), 1.4.2


## License
[![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)](https://github.com/ondrej-tucek/Machine-Learning-HAR/blob/master/LICENSE)


