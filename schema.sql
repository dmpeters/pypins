

CREATE TABLE packages (
  package_id integer primary key autoincrement,
  name string not null
);


CREATE TABLE "users" (
"user_id" integer PRIMARY KEY AUTOINCREMENT,
"name" string NOT NULL,
"oauth_token" string NOT NULL,
"oauth_secret" string NOT NULL
);


CREATE UNIQUE INDEX "index_user_name" ON "users" ("name");

CREATE TABLE "users_packages" (
"user_id" integer NOT NULL,
"package_id" integer NOT NULL,
CONSTRAINT "foreign_key_users_id" FOREIGN KEY ("user_id") REFERENCES "users"("user_id") ON DELETE CASCADE
);


CREATE INDEX "index_user_id" ON "users_packages" ("user_id");
CREATE UNIQUE INDEX "index_user_id_package_id" ON "users_packages" ("user_id", "package_id");