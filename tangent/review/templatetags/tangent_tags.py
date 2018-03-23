from django import template
from django.utils.safestring import mark_safe
from review.models import UserProfile,Review,Leave,Customer,PublicHoliday
register = template.Library()


@register.simple_tag()
def b_day(email):
    return mark_safe("<h1>" + email + "</h1>")


@register.simple_tag()
def employees():

    users = UserProfile.objects.all()


    html = """<header class="bg-turquoise text-white">
                      <h4>"""+str(len(users))+""" of Employees</h4>
                    </header>
                    <div class="box-body p-a-0 max-h-lg ps">
                      <table id="employee_stats" class="table table-inverse ps" data-plugin="tablesorter">
                        <thead>
                          <tr>
                            <th>#</th>
                            <th>First</th>
                            <th>Last</th>
                            <th>E-mail</th>
                            <th>Phone</th>
                          </tr>
                        </thead>"""

    for user in users:
        html += """    <tbody>
                          <tr>
                            <td>"""+str(user.old_id)+""" </td>
                            <td>"""+str(user.user.first_name)+"""</td>
                            <td>"""+str(user.user.last_name)+"""</td>
                            <td>"""+str(user.email)+"""</td>
                            <td>"""+str(user.phone_number)+"""</td>
                          </tr>
                        </tbody> """ 

    html += """       </table>
                    </div>
                  </div>
                </div>"""


    return mark_safe(html)

@register.simple_tag()
def to_do():

    

    html = """<header class="b-b">
                      <h4>Todo</h4>
                    </header>
                    <div class="box-body p-a-0 max-h-lg ps">

                      <ul class="todo-list is-order dragula" data-plugin="todo">"""


    for user in UserProfile.objects.all():
        
        if user.days_to_birthday<30:



            html += """<li class="todo-item draggable handle ">
                              <a href="#" class="todo-link">
                                <i class="fa fa-fw fa-lg fa-square-o"></i>
                              </a>
                              <span class="todo-title">"""+str(user.user.first_name)+""" """+str(user.user.last_name)+""" birthday in less than a month </span>
                            </li>""" 

        if user.years_worked>5:



            html += """<li class="todo-item draggable handle ">
                              <a href="#" class="todo-link">
                                <i class="fa fa-fw fa-lg fa-square-o"></i>
                              </a>
                              <span class="todo-title">"""+str(user.user.first_name)+""" """+str(user.user.last_name)+""" has worked for at least 5 years </span>
                            </li>""" 

        if user.age>35:



            html += """<li class="todo-item draggable handle ">
                              <a href="#" class="todo-link">
                                <i class="fa fa-fw fa-lg fa-square-o"></i>
                              </a>
                              <span class="todo-title">"""+str(user.user.first_name)+""" """+str(user.user.last_name)+""" is getting old</span>
                            </li>""" 

    html += """       <!-- /.todo-item -->
                      </ul>
                      <!-- /.todo-list -->
                    </div>
                    <!-- /.box-body -->
                  </div>
                  <!-- /.box -->"""


    return mark_safe(html)

@register.simple_tag()
def gender_graph():
    gender_m    = UserProfile.objects.filter(gender="M")
    gender_f    = UserProfile.objects.filter(gender="F")
    try:
        perc = len(gender_m)/len(gender_f)*100
    except:
        perc = "12%"
    html = """  <div class="col-xs-6 col-sm-3">
                  <div class="box p-a-0 bg-peter-river b-r-3">
                    <div class="p-a-15">
                      <span class="text-white">Gender %</span>
                      <div class="f-5 text-white">
                        <span class="counterup">""" + str(perc) + """</span>
                        <span class="h4">""" + str(perc) + """
                          <i class="fa fa-fw fa-caret-up"></i>
                        </span>
                      </div>
                    </div>
                    <hr class="m-t-0 m-b-5 b-s-dashed">
                    <div><iframe class="chartjs-hidden-iframe" style="display: block; overflow: hidden; border: 0px none; margin: 0px; top: 0px; left: 0px; bottom: 0px; right: 0px; height: 100%; width: 100%; position: absolute; pointer-events: none; z-index: -1;" tabindex="-1"></iframe>
                      <canvas width="232" height="69" data-charty="statarea" data-label="Line" data-labels="['a','b','c','d','e','f','g']" data-value="[28,68,41,43,96,45,100]" data-border-color="#ffffff" data-background-color="rgba(255, 255, 255, 0.1)" style="display: block; width: 232px; height: 69px;"></canvas>
                    </div>
                  </div>
                </div>"""

    return mark_safe(html)

@register.simple_tag()
def nearest_bday():
    user_bday   = UserProfile.objects.all().order_by("days_to_birthday")
    try:
        days = int(user_bday[0].days_to_birthday)-365
        perc = int(user_bday[0].days_to_birthday)/365*100

    except:
        days = 3
        perc = "11%"

    html = """<div class="col-xs-6 col-sm-3">
                  <div class="box p-a-0 bg-concrete b-r-3">
                    <div class="p-a-15">
                      <span class="text-white">Next B-day</span>
                      <div class="f-5 text-white">
                        <span class="counterup">"""+str(days)+"""</span>
                        <span class="h4">"""+str(perc)+"""%
                          <i class="fa fa-fw fa-caret-down text-alizarin"></i>
                        </span>
                      </div>
                    </div>
                    <hr class="m-t-0 m-b-5">
                    <div><iframe class="chartjs-hidden-iframe" style="display: block; overflow: hidden; border: 0px none; margin: 0px; top: 0px; left: 0px; bottom: 0px; right: 0px; height: 100%; width: 100%; position: absolute; pointer-events: none; z-index: -1;" tabindex="-1"></iframe>
                      <canvas width="232" height="69" data-charty="statline" data-label="Line" data-labels="['a','b','c','d','e','f','g']" data-value="[43,48,52,58,50,95,100]" data-border-color="#fff" style="display: block; width: 232px; height: 69px;"></canvas>
                    </div>
                  </div>
                </div>"""

    return mark_safe(html)



@register.simple_tag()
def salary_increase():

    holiday = PublicHoliday.objects.all()
    html = """<div class="col-sm-4">
                  <div class="box shadow-2dp b-r-2">
                    <header class="b-b">
                      <h4>Holidays</h4>
                    </header>
                    <div class="box-body">
                      <ul class="tasks">"""
    for h in holiday:
        html += """<li class="task">
                          <div class="task-media bg-alizarin">
                            <i class="fa fa-fw fa-plus"></i>
                          </div>
                          <div class="task-info">
                            <a class="task-info-link" href="#">"""+str(h.name)+"""</a>
                            <div>
                              <i></i>
                              <span>"""+str(h.date)+"""</span>
                            </div>
                          </div>
                        </li>"""
    html +="""        </ul>
                    </div>
                  </div>
                </div>"""

    return mark_safe(html)

@register.simple_tag()
def review_employee():

    html = """<div class="col-sm-4">
                  <div class="box shadow-2dp">
                    <header>
                      <h4>Employee
                        <small class="text-muted">Reviews</small>
                      </h4>
                    </header>
                    <div class="box-body p-a-0">
                      <nav class="list-group m-a-0">
                        <a href="#" class="list-group-item b-r-0">
                          Gwenborough
                          <span class="pull-right">28%</span>
                          <span class="list-group-progress" style="width: 59%;"></span>
                        </a>
                        <a href="#" class="list-group-item b-r-0">
                          Wisokyburgh
                          <span class="pull-right">96%</span>
                          <span class="list-group-progress" style="width: 55%;"></span>
                        </a>
                      </nav>
                    </div>
                  </div>
                </div>"""

    return mark_safe(html)
                
                
