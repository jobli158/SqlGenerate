<template>
	<div>
		<top></top>
		<div style="margin-top: 50px;margin-left:20px ;margin-right: 20px;">
			<el-input type="textarea" :rows="8" placeholder="请输入sql语句!" v-model="sql">
			</el-input>
		</div>
		<div class="btn">
			<el-button type="primary" @click="sub()">提交</el-button>&nbsp;&nbsp;&nbsp;&nbsp;
			<el-button type="danger" @click="clear()">清空</el-button>
		</div>
		<div style="padding: 20px;">
			快捷粘贴：<br />
			查询数据：select * from 'tablename';
			<br />
			查询表存在：select count(*) from pg_class where relname = 'tablename';
			<br />
			查询当前库所有表信息：
			select * from pg_tables;
			<br />
			查询特定表名及备注：select relname as tabname,
			cast(obj_description(relfilenode,'pg_class') as varchar) as comment from pg_class c
			where relname ='tablename';
			<br />
			查询表结构：select
			a.attnum as "序号",
			c.relname as "表名",
			cast(obj_description(c.oid) as varchar) as "表名描述",
			a.attname as "列名",
			t.typname AS 字段类型,
			CASE WHEN t.typlen = -1 THEN a.atttypmod - 4 ELSE t.typlen::integer END AS 字段大小 ,
			d.description as "备注"
			from
			pg_attribute a
			left join pg_description d on
			d.objoid = a.attrelid
			and d.objsubid = a.attnum
			left join pg_class c on
			a.attrelid = c.oid
			left join pg_type t on
			a.atttypid = t.oid
			where
			a.attnum >= 0
			and c.relname like 'tablename'
			order by
			c.relname desc,
			a.attnum asc
			<br />
			删除：DROP TABLE table_name;
			<br />
			插入：INSERT INTO TABLE_NAME VALUES (value1,value2,value3,...valueN);<br />
			INSERT INTO TABLE_NAME (column1, column2, column3,...columnN)
			VALUES (value1, value2, value3,...valueN);
		</div>
		<div style="margin-top: 20px;padding: 20px;" v-show="res!=''">
			受影响行数：{{res.row}}<br /><br />
			<div>
				<el-table :data="res.result" border>
					<el-table-column :label="val" v-for="(val, i) in res.title" :key="i">
						<template slot-scope="scope">{{res.result[scope.$index][i]}}</template>
					</el-table-column>
				</el-table>
			</div>
		</div>
		<div style="height: 100px;">

		</div>
		<foot></foot>
	</div>
</template>

<script>
	import top from '../components/top.vue'
	import foot from '../components/footer.vue'
	export default {
		name: 'sql',
		data() {
			return {
				sql: '',
				res: ''
			}
		},
		components: {
			top,
			foot
		},
		methods: {
			sub() {
				let data = {
					sql: this.sql
				}
				this.res = ''
				this.$axios.post(this.$https + "/savedatabase", this.$qs.stringify(data)).then(res => {
					this.res = res.data
				}).catch(res => {
					console(res)
				})
				this.$message({
					message: '执行成功,为保证准确性，请到数据库查看！',
					type: 'success'
				});

			},
			clear() {
				this.sql = ''
			}
		}


	}
</script>

<style scoped>
	.page {
		padding: 10px;
	}

	.top {
		text-align: center;
		margin-bottom: 40px;
	}

	.btn {
		margin-top: 20px;
		text-align: center;
	}
</style>
