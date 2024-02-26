# comicpy

Tool to create CBR or CBZ files.

Extracts images from PDF, ZIP, CBR files, generating comic files respecting their original order.


> The original files are not altered.


### Important

For full operation of `comicpy` when using RAR files, you must have available the `rar` command, download and install it from the official site, [**rarlab - rar/unrar command**](https://www.rarlab.com/download.htm).


## Features

* Convert `PDF` file to `CBR` or `CBZ` files (by default).
* Convert `RAR` files to `CBR` files.
* Convert `ZIP` files to `CBZ` files.
* Scan in given directory and filter `PDF`, `ZIP`, `RAR` files depending on the given extension, convert them into `CBR` or `CBZ` files, generating individual files or consolidated into one.
* Scan in the given directory and filter `CBR`, `CBZ` files allowing to merge them all into one.
* Extract `CBR` or `CBZ` files from `RAR` or `ZIP` archives.
* Support for password protected `RAR` or `ZIP` archives.


# Installation

```
pip install comicpy
```

# Usage

## CLI - usage

Command help.

```bash
$ comicpy -h
```

### File usage

| Command | Description |
|-|-|
| --type f | File. |
| -p PATH, --path PATH | Path of file. |
| -d DEST, --dest DEST | Path to save output files. Default is "." |
| -c {rar,zip}, --compressor {rar,zip} | Type of compressor to use. |
| -o OUTPUT, --output OUTPUT | Prefix of output file. |
| --check | Check the CBR or CBZ files created. |
| -u {b,kb,mb,gb}, --unit {b,kb,mb,gb} | Unit of measure of data size. Default is "mb". |
| --password PASSWORD | Password of file protected. |

```bash
$ comicpy --type f -p file.PDF --check -u kb
$
$ comicpy --type f -p file.rar --check
$
$ comicpy --type f -p file.zip --check --password PASS
```

### Directory usage

| Command | Description |
|-|-|
| --type d | Directory. |
| -p PATH, --path PATH | Path of directory. |
| --filter {pdf,rar,zip,cbr,cbz} | Filter files on directory. Default is "zip". |
| -c {rar,zip}, --compressor {rar,zip} | Type of compressor to use. Default is "zip".|
| -d DEST, --dest DEST | Path to save output files. Default is ".".
| -o OUTPUT, --output OUTPUT | Prefix of output file. Default is "Converted_". |
| --check | Check the CBR or CBZ files created. |
| --join | Join or does not files thath are in the directory. Default is "False". |
| -u {b,kb,mb,gb}, --unit {b,kb,mb,gb} | Unit of measure of data size. Default is "mb". |
| --password PASSWORD | Password of file protected. |


```bash
$ comicpy --type d -p rars_dir --filter rar -c rar --check --join -o prefix_final_ --password PASS
$
$ for i in $(ls -d Zip_Dir_*/); do comicpy --type d -p $i --filter zip -c zip --check -o ${i: 0:-1} --join ; done
```



## Development - usage

> `path='.'` parameter of `ComicPy.to_write()`, indicates that files will be written by default to the current directory. It can be changed.

## Single PDF, RAR, ZIP file -> CBZ or CBR

```python
>>> from comicpy import ComicPy
>>>
>>> pdf_file = 'file_pdf.PDF'
>>>
>>> comic = ComicPy(unit='mb')
>>>
>>> data = comic.process_pdf(filename=pdf_file, compressor='zip')
>>>
>>> metaFileCompress = comic.to_write(listCurrentFiles=data)
>>> print(metaFileCompress)
[{'name': './file_pdf/file_pdf.cbz', 'size': '76.63 MB'}]
>>>
>>> comic.check_integrity(filename=metaFileCompress[0]['name'])
File is valid?:  "True"
True
>>>
>>> comic.check_integrity(filename=metaFileCompress[0]['name'], show=False)
True
>>>
```

## Directory with PDFs, RARs, ZIPs files -> CBZ or CBR

> The `join` parameter indicates whether all found files are merged or treated as individual files.


* Example, directory with RAR files - `join=False`


```python
>>> from comicpy import ComicPy
>>>
>>> dir_RAR = 'rars'
>>>
>>> comic = ComicPy(unit='GB')
>>>
>>> data = comic.process_dir(
...             filename='final_CBR_file',
...             directory_path=dir_RAR,
...             extention_filter='rar',
...             compressor='rar',
...             password=None,
...             join=False
...           )
>>> metaFileCompress = comic.to_write(listCurrentFiles=data)
>>> print(metaFileCompress)
[{'name': './final_CBR_file/chapter_1.cbr', 'size': '0.02 GB'}, {'name': './final_CBR_file/chapter_2.cbr', 'size': '0.01 GB'}, {'name': './final_CBR_file/chapter_3.cbr', 'size': '0.01 GB'}, {'name': './final_CBR_file/chapter_4.cbr', 'size': '0.01 GB'}]
>>>>
>>> for item in metaFileCompress:
...   comic.check_integrity(filename=item['name'], show=True)
...
File is valid?:  "True"
True
File is valid?:  "True"
True
File is valid?:  "True"
True
File is valid?:  "True"
True
>>>
```


* Example, directory with RAR files - `join=True`

```python
>>> from comicpy import ComicPy
>>>
>>> dir_RAR = 'rars'
>>>
>>> comic = ComicPy(unit='GB')
>>>
>>> data = comic.process_dir(
...                 filename='final_CBR_file',
...                 directory_path=dir_RAR,
...                 extention_filter='rar',
...                 compressor='rar',
...                 password=None,
...                 join=True
...               )
>>> metaFileCompress = comic.to_write(listCurrentFiles=data)
>>> print(metaFileCompress)
[{'name': 'result/final_CBR_file/final_CBR_file.cbr', 'size': '0.05 GB'}]
>>>
>>> for item in metaFileCompress:
...   comic.check_integrity(filename=item['name'], show=True)
...
File is valid?:  "True"
True
>>>
```
