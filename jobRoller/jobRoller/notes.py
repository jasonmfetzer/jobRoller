


{% load widget_tweaks %}

<div class='jumbotron'>

{% block content %}
  <form method="get">
    <div class="well">
      <h4 style="margin-top: 0">Filter</h4>
      <div class="row">
        <div class="form-group col-sm-4 col-md-3">
          {{ filter.course_id.label_tag }}
          {% render_field filter.form.course_id class="form-control" %}
        </div>
        <div class="form-group col-sm-4 col-md-3">
          {{ filter.form.course_name.label_tag }}
          {% render_field filter.form.course_name class="form-control" %}
        </div>
        <div class="form-group col-sm-4 col-md-3">
          {{ filter.form.course_pneumonic.label_tag }}
          {% render_field filter.form.course_pneumonic class="form-control" %}
        </div>
        
        <div class="form-group col-sm-8 col-md-6">
          {{ filter.form.required.label_tag }}
          <div>
            {% for choice in filter.form.required %}
              <label class="checkbox-inline">
                {{ choice.tag }} {{ choice.choice_label }}
              </label>
            {% endfor %}
          </div>
        </div>
      </div>
      <button type="submit" class="btn btn-primary">
        <span class="glyphicon glyphicon-search"></span> Search
      </button>
    </div>
  </form>
</div>
  <table class="table table-bordered">
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Pneumonic</th>
    	<th>IIT Course ID</th>
        <th>Required</th>
      </tr>
    </thead>
    <tbody>
      {% for course in filter.qs %}
        <tr>
          <td>{{ course.id }}</td>
          <td>{{ course.course_pneumonic }}</td>
          <td>{{ course.course_id }}</td>
          <td>{{ course.course_name }}</td>
          <td>
            {% for group in course.required.all %}
              {{ group }}
            {% empty %}
              <em class="text-muted">Not Required</em>
            {% endfor %}
          </td>
        </tr>
      {% empty %}
        <tr>
          <td colspan="5">No data</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}


<form>
  <div class="form-group row">
    <label for="inputEmail3" class="col-sm-2 col-form-label">Email</label>
    <div class="col-sm-10">
      <input type="email" class="form-control" id="inputEmail3" placeholder="Email">
    </div>
  </div>
  <div class="form-group row">
    <label for="inputPassword3" class="col-sm-2 col-form-label">Password</label>
    <div class="col-sm-10">
      <input type="password" class="form-control" id="inputPassword3" placeholder="Password">
    </div>
  </div>
  <fieldset class="form-group">
    <div class="row">
      <legend class="col-form-label col-sm-2 pt-0">Radios</legend>
      <div class="col-sm-10">
        <div class="form-check">
          <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios1" value="option1" checked>
          <label class="form-check-label" for="gridRadios1">
            First radio
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios2" value="option2">
          <label class="form-check-label" for="gridRadios2">
            Second radio
          </label>
        </div>
        <div class="form-check disabled">
          <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios3" value="option3" disabled>
          <label class="form-check-label" for="gridRadios3">
            Third disabled radio
          </label>
        </div>
      </div>
    </div>
  </fieldset>
  <div class="form-group row">
    <div class="col-sm-2">Checkbox</div>
    <div class="col-sm-10">
      <div class="form-check">
        <input class="form-check-input" type="checkbox" id="gridCheck1">
        <label class="form-check-label" for="gridCheck1">
          Example checkbox
        </label>
      </div>
    </div>
  </div>
  <div class="form-group row">
    <div class="col-sm-10">
      <button type="submit" class="btn btn-primary">Sign in</button>
    </div>
  </div>
</form>