from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('id', show=False)
    name_equipment = Col('Name Equipment')
    type_equipment = Col('Type Equipment')
    make_country = Col('Make in country')
    price = Col('price')
    purpose = Col('purpose')
    trainer_name = Col('trainer_name')
    class_name = Col('class_name')
    room = Col('room')
    time_of_class = Col('time_of_class')
    edit = LinkCol('Edit', 'edit_equipment', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete_equipment', url_kwargs=dict(id='id'))



    