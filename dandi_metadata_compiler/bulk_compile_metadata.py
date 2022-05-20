from pathlib import Path
from argparse import ArgumentParser

import tqdm
from dandi_metadata_compiler import DandiMetadataCompiler


def main():
    parser = ArgumentParser()
    parser.add_argument("input_dir", metavar="input_dir", type=str, nargs=1, help="Input directory")
    parser.add_argument("-c", "--config", metavar="config.yml", type=str, nargs=1, help="Config file, required",
                        required=True, dest="config")
    parser.add_argument("-o", "--output", metavar="output_dir", type=str, nargs=1,
                        help="Output directory, defaults to input directory",
                        required=False, default=None, dest="output_dir")
    parser.add_argument("--noxml", action="store_true", help="Do not create xml file", required=False)
    parser.add_argument("--nojson", action="store_true", help="Do not create json file", required=False)
    parser.add_argument("--nosymlinks", action="store_true", help="Do not create symlinks", required=False)

    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir) if args.output_dir else input_dir
    if not output_dir.is_dir():
        output_dir.mkdir(parents=True)
    write_xml = not args.noxml
    write_json = not args.nojson
    write_symlinks = not args.nosymlinks

    acquisition_dirs = list(input_dir.glob("*_*_*_LeftDet_*_RightDet_*"))
    acquisition_dirs.sort()

    for acquisition_dir in tqdm.tqdm(acquisition_dirs):

        left_dir = acquisition_dir.joinpath("tiff_left")
        right_dir = acquisition_dir.joinpath("tiff_right")




