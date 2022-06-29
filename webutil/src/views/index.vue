<template>
	<div>
		<top></top>
		<div class="top" style="margin-left: 20px;margin-right: 20px;">
			<div style="flex: 2;padding: 5px;">
				<el-input v-model="ztablename" placeholder="中文表名"></el-input>
			</div>
			<div style="flex: 2;padding: 5px;">
				<el-input v-model="tablename" placeholder="英文表名"></el-input>
			</div>
			<div style="flex: 3;padding: 5px;">
				<el-select v-model="value" clearable placeholder="请选择行业名称">
					<el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
					</el-option>
				</el-select>
			</div>
			<div style="flex: 3;line-height: 50px;">
				<el-button style="width: 120px;" type="primary" @click="constructdatabase()"  >查看表结构</el-button>&nbsp;&nbsp;&nbsp;&nbsp;
				<el-button style="width: 120px;" type="primary" @click="searchdatabase()"  >查看表数据</el-button>&nbsp;&nbsp;&nbsp;&nbsp;
				<router-link to="/detail"><span style="color: #1989fa;font-weight: bold;">查看已保存插入sql</span></router-link>
			</div>
		</div>

		<div class="mid" style="margin-left: 20px;margin-right: 20px;">
			<div style="flex: 1;padding-right: 20px;">
				<el-input type="textarea" :rows="16" placeholder="请输入行政区划 行政区划名称等....以空格隔开,每行以中文句号结尾" v-model="predata">
				</el-input>
			</div>
			<div style="flex: 1;">
				<el-input type="textarea" :rows="16" placeholder="请输入年份 数据等....以空格隔开,每行以中文句号结尾" v-model="data">
				</el-input>
			</div>
		</div>
		<div style="margin-top: 20px;text-align: center;">
			<el-button style="width: 100px;" type="primary" @click="sub()">提交</el-button>
			&nbsp;&nbsp;&nbsp;&nbsp;
			<el-button style="width: 100px;" type="danger" @click="clear()" >清空</el-button>
		</div>
		<div>
			<div style="margin-top: 20px;" v-show="isshow">
				    <p>人大金仓</p>
					<ol>
						<div v-for="item,key in rdata">
							<li>{{item.rdsql}}</li>
						</div>
					</ol>
					<br/>
					<br/>
					 <p>hlive</p>
					<ol>
						<div v-for="item,key in rdata">
							<li>{{item.hasql}}</li>
						</div>
					</ol>
					<!-- select count(*) from pg_class where relname = 't_trade_goods_f_admdiv'; -->
					<div style="text-align: center;">
						<el-button style="width: 100px;" type="primary" @click="save()" >保存本地</el-button>
						<el-button style="width: 100px;" type="primary" @click="savedatabase()"  >插入数据</el-button>
					</div>
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
		data() {
			return {
				options: [{
				 	value: '国民经济核算',
						label: '国民经济核算'
					}, {
						value: '固定资产投资',
						label: '固定资产投资'
					}, {
						value: '对外经济贸易',
						label: '对外经济贸易'
					}, {
						value: '价格',
				  label: '价格'
					}, {
						value: '财政',
						label: '财政'
					},
					{
						value: '金融业',
						label: '金融业'
					},
					{
						value: '保险业',
						label: '保险业'
					},
					{
						value: '农业',
						label: '农业'
					},
					{
						value: '工业',
						label: '工业'
					},
					{
						value: '建筑业',
						label: '建筑业'
					}, {
						value: '科技',
						label: '科技'
					}, {
						value: '能源',
						label: '能源'
					}, {
						value: '交通运输',
						label: '交通运输'
					}, {
						value: '房地产',
						label: '房地产'
					}, {
						value: '批发与零售',
						label: '批发与零售'
					}, {
						value: '经济安全保障',
						label: '经济安全保障'
					}, {
						value: '人口',
						label: '人口'
					},
					{
						value: '就业人员和工资',
						label: '就业人员和工资'
					}, {
						value: '人民生活',
						label: '人民生活'
					}, {
						value: '生态环境保护',
						label: '生态环境保护'
					}, {
						value: '绿色生态',
						label: '绿色生态'
					}, {
						value: '邮电和软件业',
						label: '邮电和软件业'
					}, {
						value: '住宿和餐饮业',
						label: '住宿和餐饮业'
					}, {
						value: '旅游业',
						label: '旅游业'
					}, {
						value: '教育',
						label: '教育'
					}, {
						value: '社会服务',
						label: '社会服务'
					}
				],
				value: '',
				ztablename: '',
				tablename: '',
				data: '',
				predata: '',
				rdata:[],
				isshow:false,
				res:''
			}
		},
		components:{
			top,
			foot
		},
		methods:{
			sub(){
				this.isshow= true
				let data = {
					hangye:this.value,
					ztablename:this.ztablename,
					tablename:this.tablename,
					data:this.data,
					predata:this.predata
				}
			this.$axios.post(this.$https,this.$qs.stringify(data)).then(res=>{
					this.rdata = res.data.data
				}).catch(res=>{
					console(res)
				})
			},
			clear(){
				this.value=''
				this.ztablename = ''
				this.tablename = ''
				this.data = ''
				this.predata = ''
				this.rdata = []
				this.res = ''
				this.isshow = false
			},
			save(){
				let rdsql = ''
				let hasql = ''
				rdsql +='--'+this.ztablename+'('+this.tablename+')\n'
				hasql +='--'+this.ztablename+'('+this.tablename+')\n'
				for(let i =0;i<this.rdata.length;i++){
					rdsql += this.rdata[i].rdsql+'\n'
					hasql += this.rdata[i].hasql+'\n'
				}
				let data = {
					hangye:this.value,
					ztablename:this.ztablename,
					tablename:this.tablename,
					rsql:rdsql,
					hsql:hasql
				}
				this.$axios.post(this.$https+"/save",this.$qs.stringify(data)).then(res=>{
					if(res.status==200){
						this.$message({ message:'保存成功！',type: 'success'});
					}else{
						this.$message.error( '保存失败！');
					}
				}).catch(res=>{
					console(res)
				})
			},
			savedatabase(){
				let word = ''
				console.log(this.rdata)
				for(let i=0;i<this.rdata.length;i++){
					word += this.rdata[i].rdsql
				}
				let data = {
					sql:word
				}
				this.$axios.post(this.$https+"/savedatabase",this.$qs.stringify(data)).then(res=>{
					this.res = res.data
					if(res.status==200){
						this.$message({ message:'执行成功！',type: 'success'});
					}else{
						this.$message.error( '保存失败！');
					}
				}).catch(res=>{
					console(res)
				})
				this.$message({ message:'执行成功,为保证准确性，请到数据库查看！',type: 'success'});
			},
			searchdatabase(){
				// let word = "select count(*) from pg_class where relname = '"+this.tablename+"';"
				let word = "select * from "+this.tablename+';'
				let data = {
					sql:word
				}
				this.$axios.post(this.$https+"/savedatabase",this.$qs.stringify(data)).then(res=>{
					this.res = res.data
					this.$message({ message:'数据查询成功',type: 'success'})
				}).catch(res=>{
					this.$message({ message:'数据查询失败',type: 'error'})
				})
			},
			constructdatabase(){
				let word = "select a.attnum AS 序号,c.relname AS 表名,cast(obj_description(c.oid) AS varchar) AS 表名描述,a.attname AS 列名,t.typname AS 字段类型,CASE WHEN t.typlen = -1 THEN a.atttypmod - 4 ELSE t.typlen::integer END AS 字段大小 ,d.description AS 备注 from pg_attribute a left join pg_description d on d.objoid = a.attrelid and d.objsubid = a.attnum left join pg_class c on a.attrelid = c.oid left join pg_type t on a.atttypid = t.oid where a.attnum >= 0 and c.relname like  '"+ this.tablename+"'  order by c.relname desc,a.attnum asc;"
				let data = {
					sql:word
				}
				this.$axios.post(this.$https+"/savedatabase",this.$qs.stringify(data)).then(res=>{
					this.res = res.data
				}).catch(res=>{
					console(res)
				})
			}

		}

	}
</script>

<style scoped>
	.top {
		display: flex;
		margin-top: 50px;
	}
	.mid{
		display: flex;
		margin-top: 20px;
	}
</style>
