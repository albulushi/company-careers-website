from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string, connect_args={
                          "ssl": {
                              "ssl_ca": "/etc/ssl/cert.pem",
                              # "cert": "/home/gord/client-ssl/client-cert.pem",
                              # "key": "/home/gord/client-ssl/client-key.pem"
                          }
                      })
  
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"select * from jobs where id = :val"), {"val":id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      # return dict(rows[0:1]._mapping])
      return dict(rows[0]._mapping)




      
# def show_data(id):
#   jobs = load_jobs_from_db()
#   # for job in jobs:
#   #   if job['id']==id:
#   #     print(job)
#   job = [job for job in jobs if job['id'] == id]
#   return job
#   # return jsonify(job=job[0])
#   # return render_template('job.html', job=job[0])
# show_data(1)