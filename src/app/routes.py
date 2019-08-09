from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, SampleForm, BatchForm, LocationForm, Result1Form, Result2Form,StudyForm, Sample_studyForm  
from app.models import User, Sample, Result1,Result2, Batch,Location,Study,Sample_study


@app.route('/')
@app.route('/index')
@login_required
def index():
    """[summary]
    
    Returns:
        [type] -- [description]
    """
 
    posts = [
        {
            'author': {'username': 'Oucru'},
            'body': 'Welcome to Seqbox Plateform!'
        }
        
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """[summary]
    
    Returns:
        [type] -- [description]
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    """[summary]
    
    Returns:
        [type] -- [description]
    """
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """[summary]
    
    Returns:
        [type] -- [description]
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/sample', methods=['GET', 'POST'])
def sample():
    """[summary]
    
    Returns:
        [type] -- [description]
    """
    form = SampleForm()
    if form.validate_on_submit():
        sample = Sample(id_sample=form.id_sample.data, num_seq=form.num_seq.data, date_time=form.date_time.data, organism=form.organism.data, location=form.location.data, batch=form.batch.data, path_r1=form.path_r1.data, path_r2=form.path_r2,result1=form.result1.data,result2=form.result2.data)
        db.session.add(sample)
        db.session.commit()
        flash('Congratulations, you are now a registered sample!')
        return redirect(url_for('index'))
    return render_template('sample.html', title='validate', form=form)

@app.route('/batch', methods=['GET', 'POST'])
def batch():
    form = BatchForm()
    if form.validate_on_submit():
        batch = Batch(id_batch=form.id_batch.data, name_batch=form.name_batch.data, date_batch=form.date_batch.data, instrument=form.instrument.data, primer=form.primer.data)
        db.session.add(batch)
        db.session.commit()
        flash('Congratulations, you are now a registered batch!')
        return redirect(url_for('index'))
    return render_template('batch.html', title='validate', form=form)

@app.route('/location', methods=['GET', 'POST'])
def location():
    form = LocationForm()
    if form.validate_on_submit():
        location = Location(id_location=form.id_location.data, continent=form.continent.data, country=form.country.data, province=form.province.data, city=form.city.data)
        db.session.add(location)
        db.session.commit()
        flash('Congratulations, you are now a registered location!')
        return redirect(url_for('index'))
    return render_template('location.html', title='validate', form=form)

@app.route('/result1', methods=['GET', 'POST'])
def result1():
    form = Result1Form()
    if form.validate_on_submit():
        result1 = Result1(id_result1=form.id_result1.data, qc=form.qc.data, ql=form.ql.data, description=form.description.data, snapper_variants=form.snapper_variants.data, snapper_ignored=form.snapper_ignored.data, num_heterozygous=form.num_heterozygous.data, mean_depth=form.mean_depth.data, coverage=form.coverage.data)
        db.session.add(result1)
        db.session.commit()
        flash('Congratulations, you are now a registered result1!')
        return redirect(url_for('index'))
    return render_template('result1.html', title='validate', form=form)

@app.route('/result2', methods=['GET', 'POST'])
def result2():
    form = Result2Form()
    if form.validate_on_submit():
        result2 = Result2(id_result2=form.id_result2.data, mykrobe_version=form.mykrobe_version.data, phylo_grp=form.phylo_grp.data, phylo_grp_covg=form.phylo_grp_covg.data, phylo_grp_depth=form.phylo_grp_depth.data, species=form.species.data, species_covg=form.species_covg.data, species_depth=form.species_depth.data, lineage=form.lineage.data, lineage_covg=form.lineage_covg.data, lineage_depth=form.lineage_depth.data, susceptibility=form.susceptibility.data,variants=form.variants.data,genes=form.genes.data,drug=form.drug.data)
        db.session.add(result2)
        db.session.commit()
        flash('Congratulations, you are now a registered result2!')
        return redirect(url_for('index'))
    return render_template('result2.html', title='validate', form=form)

@app.route('/study', methods=['GET', 'POST'])
def study():
    form = StudyForm()
    if form.validate_on_submit():
        study = Study(id_study=form.id_study.data, date_study=form.date_study.data, result_study=form.result_study.data)
        db.session.add(study)
        db.session.commit()
        flash('Congratulations, you are now a registered study!')
        return redirect(url_for('index'))
    return render_template('study.html', title='validate', form=form)

@app.route('/sample_study', methods=['GET', 'POST'])
def sample_study():
    form = Sample_studyForm()
    if form.validate_on_submit():
        sample_study = Sample_study(id_sample=form.id_sample.data,id_study=form.id_study.data)
        db.session.add(sample_study)
        db.session.commit()
        flash('Congratulations, you are now a registered sample_study!')
        return redirect(url_for('index'))
    return render_template('sample_study.html', title='validate', form=form)