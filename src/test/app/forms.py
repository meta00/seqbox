
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User, Sample


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class SampleForm(FlaskForm):
    id_sample = StringField('id_sample', validators=[DataRequired()])
    num_seq = StringField('num_seq', validators=[DataRequired()])
    date_time = StringField('date_time',validators=[DataRequired()])
    organism = StringField('organism',validators=[DataRequired()])
    path_r1 = StringField('path_r1',validators=[DataRequired()])
    path_r2 = StringField('path_r2',validators=[DataRequired()])
    batch =  StringField('batch',validators=[DataRequired()])
    location = StringField('location',validators=[DataRequired()])
    result1 = StringField('result1',validators=[DataRequired()])
    result2 = StringField('result2',validators=[DataRequired()])

    submit = SubmitField('Validate')

    def validate_id_sample(self, id_sample):
        sample = Sample.query.filter_by(id_sample=id_sample.data).first()
        if sample is not None:
            raise ValidationError('Please use a different id_sample.')
    
    def validate_num_seq(self,num_seq):
        sample =Sample.query.filter_by(num_seq=num_seq.data).first()
        if sample is not None:
            raise ValidationError('Please use a different num_seq.')

    def validate_date_time(self,date_time):
        sample =Sample.query.filter_by(date_time=date_time.data).first()
        if sample is not None:
            raise ValidationError('Please use a different date_time.')

    def validate_organism(self, organism):
        sample = Sample.query.filter_by(organism=organism.data).first()
        if sample is not None:
            raise ValidationError('Please use a different organism.')
    
    def validate_path_r1(self, path_r1):
        sample = Sample.query.filter_by(path_r1=path_r1.data).first()
        if sample is not None:
            raise ValidationError('Please use a different path_r1.')

    def validate_path_r2(self, path_r2):
        sample = Sample.query.filter_by(path_r2=path_r2.data).first()
        if sample is not None:
            raise ValidationError('Please use a different path_r2.')

    def validate_batch(self,  batch):
        sample = Sample.query.filter_by( batch= batch.data).first()
        if sample is not None:
            raise ValidationError('Please use a different  batch.')
    
    def validate_location(self,location):
        sample =Sample.query.filter_by(location=location.data).first()
        if sample is not None:
            raise ValidationError('Please use a different location.')

    def validate_result1(self,result1 ):
        sample =Sample.query.filter_by(result1 =result1.data).first()
        if sample is not None:
            raise ValidationError('Please use a different result1 .')
    
    def validate_result2(self,result2):
        sample =Sample.query.filter_by(result2=result2.data).first()
        if sample is not None:
            raise ValidationError('Please use a different result2.')


class BatchForm(FlaskForm):
    id_batch = StringField('id_batch', validators=[DataRequired()])
    name_batch = StringField('name_batch', validators=[DataRequired()])
    date_batch = StringField('date_batch',validators=[DataRequired()])
    instrument = StringField('instrument',validators=[DataRequired()])
    primer = StringField('primer',validators=[DataRequired()])
    
    submit = SubmitField('Validate')

    def validate_id_batch(self, id_batch):
        batch = Batch.query.filter_by(id_batch=id_batch.data).first()
        if batch is not None:
            raise ValidationError('Please use a different id_batch.')

    def validate_name_batch(self, name_batch):
        batch = Batch.query.filter_by(name_batch=name_batch.data).first()
        if batch is not None:
            raise ValidationError('Please use a different name_batch.')

    def validate_date_batch(self, date_batch):
        batch = Batch.query.filter_by(date_batch=date_batch.data).first()
        if batch is not None:
            raise ValidationError('Please use a different date_batch.')

    def validate_instrument(self, instrument):
        batch = Batch.query.filter_by(instrument=instrument.data).first()
        if batch is not None:
            raise ValidationError('Please use a different instrument.')
    
    def validate_primer(self, primer):
        batch = Batch.query.filter_by(primer=primer.data).first()
        if batch is not None:
            raise ValidationError('Please use a different primer.')
    

class LocationForm(FlaskForm):
    id_location= StringField('id_location', validators=[DataRequired()])
    continent = StringField('continent', validators=[DataRequired()])
    country = StringField('country',validators=[DataRequired()])
    province = StringField('province',validators=[DataRequired()])
    city = StringField('city',validators=[DataRequired()])

    submit = SubmitField('Validate')

    def validate_id_location(self, id_location):
        location = Location.query.filter_by(id_location=id_location.data).first()
        if location is not None:
            raise ValidationError('Please use a different id_location.')

    def validate_continent(self, continent):
        location = Location.query.filter_by(continent=continent.data).first()
        if location is not None:
            raise ValidationError('Please use a different continent.')

    def validate_country(self, country):
        location = Location.query.filter_by(country=country.data).first()
        if location is not None:
            raise ValidationError('Please use a different country.')
    
    def validate_province(self, province):
        location = Location.query.filter_by(province=province.data).first()
        if location is not None:
            raise ValidationError('Please use a different province.')
    
    def validate_city(self, city):
        location = Location.query.filter_by(city=city.data).first()
        if location is not None:
            raise ValidationError('Please use a different city.')

class Result1Form(FlaskForm):
    id_result1= StringField('id_result1', validators=[DataRequired()])
    qc = StringField('qc', validators=[DataRequired()])
    ql = StringField('ql',validators=[DataRequired()])
    description = StringField('description',validators=[DataRequired()])
    snapper_variants = StringField('snapper_variants',validators=[DataRequired()])
    snapper_ignored = StringField('snapper_ignored',validators=[DataRequired()])
    num_heterozygous = StringField('num_heterozygous',validators=[DataRequired()])
    mean_depth = StringField('mean_depth',validators=[DataRequired()])
    coverage = StringField('coverage',validators=[DataRequired()])

    submit = SubmitField('Validate')

    def validate_id_result1(self, id_result1):
        result1 = Result1.query.filter_by(id_result1=id_result1.data).first()
        if result1 is not None:
            raise ValidationError('Please use a different id_result1.')

    def validate_qc(self, qc):
        result1 = Result1.query.filter_by(qc=qc.data).first()
        if result1 is not None:
            raise ValidationError('Please use a different qc.')

    def validate_ql(self, ql):
        result1 = Result1.query.filter_by(ql=ql.data).first()
        if result1 is not None:
            raise ValidationError('Please use a different ql.')

    def validate_description(self, description):
        result1 = Result1.query.filter_by(description=description.data).first()
        if result1 is not None:
            raise ValidationError('Please use a different description.')

    def validate_snapper_variants(self, snapper_variants):
        result1 = Result1.query.filter_by(snapper_variants=snapper_variants.data).first()
        if result1 is not None:
            raise ValidationError('Please use a different snapper_variants.')

    def validate_snapper_ignored(self, snapper_ignored):
        result1 = Result1.query.filter_by(snapper_ignored=snapper_ignored.data).first()
        if result1 is not None:
            raise ValidationError('Please use a different snapper_ignored.')

    def validate_num_heterozygous(self, num_heterozygous):
        result1 = Result1.query.filter_by(num_heterozygous=num_heterozygous.data).first()
        if result1 is not None:
            raise ValidationError('Please use a different num_heterozygous.')

    def validate_mean_depth(self, mean_depth):
        result1 = Result1.query.filter_by(mean_depth=mean_depth.data).first()
        if result1 is not None:
            raise ValidationError('Please use a different mean_depth.')

    def validate_coverage(self, coverage):
        result1 = Result1.query.filter_by(coverage=coverage.data).first()
        if result1 is not None:
            raise ValidationError('Please use a different coverage.')    

class Result2Form(FlaskForm):
    id_result2= StringField('id_result2', validators=[DataRequired()])
    mykrobe_version = StringField('mykrobe_version', validators=[DataRequired()])
    phylo_grp = StringField('phylo_grp',validators=[DataRequired()])
    phylo_grp_covg = StringField('phylo_grp_covg',validators=[DataRequired()])
    phylo_grp_depth = StringField('phylo_grp_depth',validators=[DataRequired()])
    species = StringField('species',validators=[DataRequired()])
    species_covg = StringField('species_covg',validators=[DataRequired()])
    species_depth = StringField('species_depth',validators=[DataRequired()])
    lineage = StringField('lineage',validators=[DataRequired()])
    lineage_covg = StringField('lineage_covg',validators=[DataRequired()])
    lineage_depth = StringField('lineage_depth',validators=[DataRequired()])
    susceptibility = StringField('susceptibility',validators=[DataRequired()])
    variants = StringField('variants',validators=[DataRequired()])
    genes = StringField('genes',validators=[DataRequired()])
    drug = StringField('drug',validators=[DataRequired()])

    submit = SubmitField('Validate')

    def validate_id_result2(self, id_result2):
        result2 = Result2.query.filter_by(id_result2=id_result2.data).first()
        if result2 is not None:
            raise ValidationError('Please use a different id_result2.')

    def validate_mykrobe_version(self, mykrobe_version):
        result2 = Result2.query.filter_by(mykrobe_version=mykrobe_version.data).first()
        if result2 is not None:
            raise ValidationError('Please use a different mykrobe_version.')
    
    def validate_phylo_grp(self, phylo_grp):
        result2 = Result2.query.filter_by(phylo_grp=phylo_grp.data).first()
        if result2 is not None:
            raise ValidationError('Please use a different phylo_grp.')
    
    def validate_phylo_grp_covg(self, phylo_grp_covg):
        result2 = Result2.query.filter_by(phylo_grp_covg=phylo_grp_covg.data).first()
        if result2 is not None:
            raise ValidationError('Please use a different phylo_grp_covg.')
    
    def validate_phylo_grp_depth(self, phylo_grp_depth):
        result2 = Result2.query.filter_by(phylo_grp_depth=phylo_grp_depth.data).first()
        if result2 is not None:
            raise ValidationError('Please use a different phylo_grp_depth.')

    def validate_species(self, species):
        result2 = Result2.query.filter_by(species=species.data).first()
        if result2 is not None:
            raise ValidationError('Please use a different species.')
    
    def validate_species_covg(self, species_covg):
        result2 = Result2.query.filter_by(species_covg=species_covg.data).first()
        if result2 is not None:
            raise ValidationError('Please use a different species_covg.')
    
    def validate_species_depth(self, species_depth):
        result2 = Result2.query.filter_by(species_depth=species_depth.data).first()
        if result2 is not None:
            raise ValidationError('Please use a different species_depth.')
    
    def validate_lineage(self, lineage):
        result2 = Result2.query.filter_by(lineage=lineage.data).first()
        if result2 is not None:
            raise ValidationError('Please use a different lineage.')
    
    def validate_lineage_covg(self, lineage_covg):
        result2 = Result2.query.filter_by(lineage_covg=lineage_covg.data).first()
        if result2 is not None:
            raise ValidationError('Please use a different lineage_covg.')

    def validate_lineage_depth(self, lineage_depth):
        result2 = Result2.query.filter_by(lineage_depth=lineage_depth.data).first()
        if result2 is not None:
            raise ValidationError('Please use a different lineage_depth.')

    def validate_susceptibility(self, susceptibility):
        result2 = Result2.query.filter_by(susceptibility=susceptibility.data).first()
        if result2 is not None:
            raise ValidationError('Please use a different susceptibility.')
    
    def validate_variants(self, variants):
        result2 = Result2.query.filter_by(variants=variants.data).first()
        if result2 is not None:
            raise ValidationError('Please use a different variants.')
    

    def validate_genes(self, genes):
        result2 = Result2.query.filter_by(genes=genes.data).first()
        if result2 is not None:
            raise ValidationError('Please use a different genes.')
    
    def validate_drug(self, drug):
        result2 = Result2.query.filter_by(drug=drug.data).first()
        if result2 is not None:
            raise ValidationError('Please use a different drug.')


class StudyForm(FlaskForm):
    id_study = StringField('id_study', validators=[DataRequired()])
    date_study = StringField('date_study', validators=[DataRequired()])
    result_study = StringField('result_study',validators=[DataRequired()])

    def validate_id_study(self, id_study):
        study = Study.query.filter_by(id_study=id_study.data).first()
        if study is not None:
            raise ValidationError('Please use a different id_study.')
    

    def validate_date_study(self, date_study):
        study = Study.query.filter_by(date_study=date_study.data).first()
        if study is not None:
            raise ValidationError('Please use a different date_study.')

    def validate_result_study(self, result_study):
        study = Study.query.filter_by(result_study=result_study.data).first()
        if study is not None:
            raise ValidationError('Please use a different result_study.')


class Sample_studyForm(FlaskForm):
    id_study = StringField('id_study', validators=[DataRequired()])
    id_sample = StringField('id_sample', validators=[DataRequired()])
    

    def validate_id_study(self, id_study):
        sample_study = Sample_study.query.filter_by(id_study=id_study.data).first()
        if sample_study is not None:
            raise ValidationError('Please use a different id_study.')

    def validate_id_sample(self, id_sample):
        sample_study = Sample_study.query.filter_by(id_sample=id_sample.data).first()
        if sample_study is not None:
            raise ValidationError('Please use a different id_sample.')