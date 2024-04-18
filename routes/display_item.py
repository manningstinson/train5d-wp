
from flask import render_template
from db_config import DBConfig

@app.route('/display_item/<int:item_id>')
def display_item(item_id):
        try:
            # Create SQLAlchemy engine using DBConfig
            engine = DBConfig.create_engine()
            connection = engine.connect()

            # Example query to fetch item by ID
            query = "SELECT * FROM ex_list WHERE id = %s"
            result = connection.execute(query, (item_id,))
            item = result.fetchone()

            connection.close()

            # Render template to display item
            return render_template('display_item.html', item=item)

        except Exception as e:
            return "Error: " + str(e)