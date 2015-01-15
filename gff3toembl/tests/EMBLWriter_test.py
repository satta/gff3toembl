import unittest
import sys
import os
import filecmp
from gff3toembl.EMBLWriter import EMBLWriter
from gff3toembl import convert

modules_dir = os.path.dirname(os.path.abspath(convert.__file__))
data_dir = os.path.join(modules_dir, 'tests', 'data')

class TestEMBLWriter(unittest.TestCase):

    def test_single_feature(self):
        '''test that the script will convert from GFF3 to EMBL'''
        emblwriter = EMBLWriter(os.path.join(data_dir,'single_feature.gff'), 
           'Organism', 
           1234, 
           'My project', 
           'My description', 
           'John', 
           'Some title',  
           'Some journal', 
           'circular', 
           'PROK', 
           'single_feature.embl', None,11,  None )
        emblwriter.parse_and_run()
        assert filecmp.cmp(os.path.join(data_dir, 'expected_single_feature.embl'), 'single_feature.embl', shallow=False)
        os.remove('single_feature.embl')
        
    def test_single_feature_new_locus_tag(self):
        '''test that the script will convert from GFF3 to EMBL and change the locus tag'''
        emblwriter = EMBLWriter(os.path.join(data_dir,'single_feature.gff'), 
           'Organism', 
           1234, 
           'My project', 
           'My description', 
           'John', 
           'Some title',  
           'Some journal', 
           'circular', 
           'PROK', 
           'single_feature.embl', 'new_locus_tag', 11, None )
        emblwriter.parse_and_run()
        assert filecmp.cmp(os.path.join(data_dir, 'expected_single_feature_new_locus_tag.embl'), 'single_feature.embl', shallow=False)
        os.remove('single_feature.embl')

    def test_single_feature_translation_table(self):
        '''test that the script will convert from GFF3 to EMBL and change the locus tag'''
        emblwriter = EMBLWriter(os.path.join(data_dir,'single_feature.gff'), 
           'Organism', 
           1234, 
           'My project', 
           'My description', 
           'John', 
           'Some title',  
           'Some journal', 
           'circular', 
           'PROK', 
           'single_feature.embl', None, 1, None )
        emblwriter.parse_and_run()
        assert filecmp.cmp(os.path.join(data_dir, 'expected_single_feature_translation_table.embl'), 'single_feature.embl', shallow=False)
        os.remove('single_feature.embl')


    def test_large_conversion(self):
        '''test a large gff3 file converts to EMBL'''
        emblwriter = EMBLWriter(os.path.join(data_dir,'large_annotation.gff'), 
           'Organism', 
           1234, 
           'My project', 
           'My description', 
           'John', 
           'Some title',  
           'Some journal', 
           'circular', 
           'PROK', 
           'large_annotation.embl', None, 11, None )
        emblwriter.parse_and_run()
        assert filecmp.cmp(os.path.join(data_dir, 'expected_large_annotation.embl'), 'large_annotation.embl', shallow=False)
        os.remove('large_annotation.embl')
        
        
    def test_chromosome_list_conversion(self):
       '''test chromosome list creation'''
       emblwriter = EMBLWriter(os.path.join(data_dir,'chromosome_list.gff'), 
          'Organism', 
          1234, 
          'ABC', 
          'My description', 
          'John', 
          'Some title',  
          'Some journal', 
          'circular', 
          'PROK', 
          'chromosome_list.embl', None, 11, 'chromosome_list.txt' )
       emblwriter.parse_and_run()
       assert filecmp.cmp(os.path.join(data_dir, 'expected_chromosome_list.txt'), 'chromosome_list.txt', shallow=False)
       os.remove('chromosome_list.embl')
       os.remove('chromosome_list.txt')
       
    def test_renaming_16s_features(self):
      '''test renaming the feature type to rRNA if the product is 16S'''
      emblwriter = EMBLWriter(os.path.join(data_dir,'input_16s.gff'), 
          'Organism', 
          1234, 
          'ABC', 
          'My description', 
          'John', 
          'Some title',  
          'Some journal', 
          'circular', 
          'PROK', 
          '16s.embl', None, 11, None )
       emblwriter.parse_and_run()
       assert filecmp.cmp(os.path.join(data_dir, 'expected_16s.embl'), '16s.embl', shallow=False)
       os.remove('16s.embl')


