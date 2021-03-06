import os
import argparse
from experiment import run_experiment, list_experiments

OUT_DIR = os.path.join(os.path.abspath('.'), 'results')

def main():
    args = parse_args()
    if not args.list and not args.experiments:
        print "Nothing to do: no experiments passed."
        print ("Did you forget the '-e' flag? Run 'python main.py --help' for "
               "more info.")
        return

    if args.list:
        print "Available experiments:"
        for exp in list_experiments(args.exp_home):
            print "\t", exp
        return

    for exp in args.experiments:
        run_experiment(
            exp,
            exp_home=args.exp_home,
            out_dir=args.outdir,
            db_name=args.dbname,
            do_run=not args.plot_only,
            do_plot=not args.run_only,
            overwrite=not args.no_overwrite,
            partition=args.partition
        )

def parse_args():
    parser = argparse.ArgumentParser(description='Run experiments on the crowd '
                                     'simulator')
    parser.add_argument('--experiments', '-e', nargs='+',
                        metavar='EXPERIMENT_NAME',
                        help=('Names of experiments to run. See --list option '
                              'for available experiments.'))
    parser.add_argument('--exp-home', default='.',
                        help=('Directory to find experiments in (defaults to '
                              '"."'))
    parser.add_argument('--dbname', '-d', default='pyharness-db',
                        help=('Postgres database to connect to. (defaults to '
                              '\'pyharness-db\')'))
    parser.add_argument('--no-overwrite', action='store_true',
                        help=('Add to existing data in database instead of '
                              'overwriting it. (defaults to False)'))
    parser.add_argument('--outdir', '-o', default=OUT_DIR,
                        help=('Directory to output data and plots to. '
                              '(defaults to \'./results/\''))
    parser.add_argument('--partition', '-s', type=int,
                        help='Partition of the grid to run the experiments on.')
    parser.add_argument('--list', '-l', action='store_true',
                        help='List available experiments and exit.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--plot-only', '-p', action='store_true',
                        help=('Only plot experimental results: don\'t re-run '
                              'the experiment.'))
    group.add_argument('--run-only', '-r', action='store_true',
                        help=('Only run the experiment: don\'t plot the '
                              'results.'))
    return parser.parse_args()
